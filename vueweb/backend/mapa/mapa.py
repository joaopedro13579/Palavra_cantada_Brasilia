from gpiozero import Button, LED
from multiprocessing import Process
import subprocess
import time

# =========================
# CONFIGURAÇÃO
# =========================

AUDIO_DEVICES = ["hw:1,0", "hw:2,0"]

BOTOES = {
    "b1": {
        "botao": Button(5, pull_up=True),
        "led": LED(17),
        "musica": "/home/pi/audio/musica1.wav"
    },
    "b2": {
        "botao": Button(6, pull_up=True),
        "led": LED(27),
        "musica": "/home/pi/audio/musica2.wav"
    },
    "b3": {
        "botao": Button(13, pull_up=True),
        "led": LED(22),
        "musica": "/home/pi/audio/musica3.wav"
    }
}

tocando = False


# =========================
# FUNÇÕES
# =========================

def tocar_audio(device, musica):
    subprocess.run([
        "aplay",
        "-D", device,
        musica
    ])


def tocar_musica(config):
    global tocando
    tocando = True

    led = config["led"]
    musica = config["musica"]

    led.on()

    processos = []
    for dev in AUDIO_DEVICES:
        p = Process(target=tocar_audio, args=(dev, musica))
        p.start()
        processos.append(p)

    # espera música terminar
    for p in processos:
        p.join()

    led.off()
    tocando = False


# =========================
# LOOP PRINCIPAL
# =========================

print("🎵 Sistema pronto. Aguardando botões...")

while True:
    if not tocando:
        for cfg in BOTOES.values():
            if cfg["botao"].is_pressed:
                tocar_musica(cfg)
                time.sleep(0.5)  # debounce simples
                break

    time.sleep(0.05)

from gpiozero import Button, LED
import subprocess
import threading
import signal

# GPIO
botao = Button(17, pull_up=True)
led = LED(27)

# Áudio
MUSICA = "/home/pi/audio/musica.wav"

DEVICES = [
    "hw:1,0",  # caixa
    "hw:2,0"   # fone
]

tocando = False

def tocar_em_device(device):
    subprocess.run([
        "aplay",
        "-D", device,
        MUSICA
    ])

def tocar_musica_dupla():
    global tocando
    if tocando:
        return

    tocando = True
    led.on()
    print("▶ Tocando música na caixa e no fone")

    threads = []

    for d in DEVICES:
        t = threading.Thread(target=tocar_em_device, args=(d,))
        t.start()
        threads.append(t)

    # espera os dois terminarem
    for t in threads:
        t.join()

    led.off()
    tocando = False
    print("⏹ Música finalizada")

botao.when_pressed = tocar_musica_dupla

print("🟢 Pronto. Pressione o botão.")
signal.pause()

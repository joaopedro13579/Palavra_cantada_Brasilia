import subprocess
from multiprocessing import Process

tracks = [
    {"file": "audio/audio01.mp3", "device": "hw:1,0"},
    {"file": "audio/audio02.mp3", "device": "hw:2,0"},
    {"file": "audio/audio03.mp3", "device": "hw:3,0"},
    {"file": "audio/audio04.mp3", "device": "hw:4,0"},
]

def loop_track(track):
    print(f"🔁 Loop: {track['file']} → {track['device']}")
    while True:
        subprocess.run([
            "aplay",
            "-D", track["device"],
            track["file"]
        ])

if __name__ == "__main__":
    processes = []

    for t in tracks:
        p = Process(target=loop_track, args=(t,))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()

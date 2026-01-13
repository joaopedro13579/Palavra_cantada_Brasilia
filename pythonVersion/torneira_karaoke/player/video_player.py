# player/video_player.py

import subprocess
import signal

class VideoPlayer:
    def __init__(self):
        self.process = None

    def play_loop(self, video_path):
        self.stop()
        self.process = subprocess.Popen(
            ["mpv", "--fs", "--loop", video_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_IGN)
        )

    def play_once(self, video_path):
        self.stop()
        subprocess.run(
            ["mpv", "--fs", video_path],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    def stop(self):
        if self.process and self.process.poll() is None:
            self.process.terminate()
            self.process = None

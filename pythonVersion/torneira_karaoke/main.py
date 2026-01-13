# main.py

from pythonVersion.torneira_karaoke.config import BASE_VIDEO, INPUT_VIDEO_MAP
from player.video_player import VideoPlayer
from inputs.input_manager import get_input_handler
import threading
import time

player = VideoPlayer()

def on_input(key):
    if key in INPUT_VIDEO_MAP:
        print(f"Input recebido: {key}")
        player.play_once(INPUT_VIDEO_MAP[key])
        time.sleep(0.2)
        player.play_loop(BASE_VIDEO)

def main():
    player.play_loop(BASE_VIDEO)

    input_handler = get_input_handler(on_input)

    input_thread = threading.Thread(target=input_handler.start)
    input_thread.daemon = True
    input_thread.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()

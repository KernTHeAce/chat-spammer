from argparse import ArgumentParser
import keyboard
import pyautogui
from pynput.mouse import Listener
import pyperclip
import time

INPUT_LOC = []
SEND_LOC = []


def on_click_input_loc(x, y, button, pressed):
    global INPUT_LOC
    INPUT_LOC = [x, y]
    return False


def on_click_send_loc(x, y, button, pressed):
    global SEND_LOC
    SEND_LOC = [x, y]
    return False


def listen_mouse(method):
    with Listener(on_click=method) as listener:
        listener.join()


def set_send(self):
    self.listen_mouse(self.on_click_send_loc)


def start_sending(number, seconds):
    for i in range(number):
        pyperclip.copy(f"Message number {i + 1}")
        pyautogui.click(x=INPUT_LOC[0], y=INPUT_LOC[1])
        pyautogui.hotkey("ctrlleft", "v")
        pyautogui.click(x=SEND_LOC[0], y=SEND_LOC[1])
        keyboard.write(f"message number {i + 1}", )
        time.sleep(seconds)


def set_coords():
    print('Choose input location')
    listen_mouse(on_click_input_loc)
    time.sleep(2)
    print('Choose send location')
    listen_mouse(on_click_send_loc)


def main():
    args = parsing()
    set_coords()
    start_sending(args.number, args.seconds)


def parsing():
    parser = ArgumentParser(description="Run Chat Spammer")
    parser.add_argument("-s", "--seconds", help="seconds between messages", type=float, default=1)
    parser.add_argument("-n", "--number", help="number of messages", type=int, default=10)
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    main()

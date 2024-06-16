import sys
import pyautogui
import time
import threading
import pyperclip
from pynput import keyboard

filepath = "C:\\Users\\astyd256\\Documents\\GitHub\\Dota2 text paster\\text.txt"
sys.stdout.reconfigure(encoding='utf-8')

with open(filepath, 'r', encoding='utf-8') as file:
    lines = [line.strip() for line in file if line.strip()]

is_playing = False
current_line = 0

def paste(text: str):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    
def send_lines():
    global current_line, is_playing
    while True:
        if is_playing:
            if current_line < len(lines):
                pyautogui.hotkey('shift', 'enter')
                paste(lines[current_line].strip())
                pyautogui.press('enter')
                current_line += 1
                time.sleep(1)  
            else:
                is_playing = False
                current_line = 0
        time.sleep(0.1)

def toggle_playback(key):
    global current_line, is_playing
    if key == keyboard.Key.page_down:
        is_playing = not is_playing
        current_line = 0

threading.Thread(target=send_lines, daemon=True).start()

def on_press(key):
    try:
        if key == keyboard.Key.page_down:
            toggle_playback(key)
    except AttributeError:
        pass

listener = keyboard.Listener(on_press=on_press)
listener.start()

try:
    while True:
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Остановка программы")

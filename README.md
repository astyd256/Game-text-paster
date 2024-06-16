# Game Text Paster

This is a fun script designed to automate the process of sending lines of text from a file into the game chat. When the script is running, it will paste text into the chat when triggered by a specific key press.

# Features

    Reads lines from a specified text file.
    Pastes lines into Dota 2 chat upon pressing the Page Down key.
    Supports UTF-8 encoded text.
    Includes adjustable delay between sending messages.

# Requirements

* Python 3.x
* pyautogui library
* pynput library
* pyperclip library


# Usage

Place the text you want to send in a file located at ```"Script folder"\text.txt```.
Run the script:

    python script_name.py


Open the game and focus on the game window.
Press the Page Down key to start sending lines from the file to the chat.
Each press of the Page Down key will toggle the sending state (start/stop).
#!/usr/bin/python3

from PIL import Image
import time
import pyscreenshot as ImageGrab
from pytesseract import image_to_string
from subprocess import Popen, PIPE

def send_command(key):
    Popen(["xdotool", "key", key], stdout=PIPE)

while True:
    img = ImageGrab.grab(bbox=(5,5,600,300)).save('ss.jpg', 'JPEG')
    #ImageGrab.grab_to_file('ss.png')
    all_text = image_to_string(Image.open('ss.jpg'))
    text = all_text.split('\n')
    for line in text:
        if 'YOU' not in line:
            print(line)
            if 'Nice' in line:
                send_command('2')
                send_command('3')
            if 'Sorry' in line:
                send_command('4')
                send_command('2')
    time.sleep(2)
import random
import time
import os

while True:
    x = random.randint(900, 1500)
    y = random.randint(400, 800)
    os.system(f"xdotool click --repeat 10 --delay 50 4")
    time.sleep(10)

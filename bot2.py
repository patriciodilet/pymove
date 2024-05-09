import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import pyautogui as pag
import random
import time
import threading

class AutoClickerApp:
    def __init__(self, master):
        self.master = master
        master.title("AutoClicker")
        master.geometry("800x400")

        style = ttk.Style(master)
        style.theme_use('equilux')

        title_label = ttk.Label(master, text="Welcome to AutoClicker", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        description_label = ttk.Label(master, text="This application will automatically move the cursor and press the Windows key every 10 seconds.", wraplength=380, justify="center")
        description_label.pack(pady=5)

        self.start_button = ttk.Button(master, text="Start", command=self.start_auto_clicker)
        self.start_button.pack(pady=10)

        self.stop_button = ttk.Button(master, text="Stop", command=self.stop_auto_clicker)
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)

        self.is_running = False
        self.timer_thread = None

    def start_auto_clicker(self):
        if not self.is_running:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.timer_thread = threading.Thread(target=self.auto_clicker_loop)
            self.timer_thread.start()

    def stop_auto_clicker(self):
        if self.is_running:
            self.is_running = False
            self.stop_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)

    def auto_clicker_loop(self):
        while self.is_running:
            x = random.randint(900, 1500)
            y = random.randint(400, 800)
            pag.moveTo(x, y, 0.2)
            pag.press("win")
            time.sleep(10)

def main():
    root = ThemedTk(theme="equilux")
    app = AutoClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

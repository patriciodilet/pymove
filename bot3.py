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

        self.user_authenticated = False
        self.autoclicker_running = False

        title_label = ttk.Label(master, text="Welcome to AutoClicker", font=("Arial", 16, "bold"))
        title_label.pack(pady=10)

        self.username_label = ttk.Label(master, text="Username:")
        self.username_label.pack()
        self.username_entry = ttk.Entry(master)
        self.username_entry.pack()

        self.password_label = ttk.Label(master, text="Password:")
        self.password_label.pack()
        self.password_entry = ttk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = ttk.Button(master, text="Login", command=self.login)
        self.login_button.pack(pady=5)

        self.clear_button = ttk.Button(master, text="Clear", command=self.clear_fields)
        self.clear_button.pack(pady=5)

        self.start_button = ttk.Button(master, text="Start", command=self.start_auto_clicker, state=tk.DISABLED)
        self.stop_button = ttk.Button(master, text="Stop", command=self.stop_auto_clicker, state=tk.DISABLED)

        self.status_label = ttk.Label(master, text="Status: Stopped", foreground="red")
        self.status_label.pack(pady=5)

        self.is_running = False
        self.timer_thread = None

    def hide_initial_elements(self):
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.password_label.pack_forget()
        self.password_entry.pack_forget()
        self.login_button.pack_forget()
        self.clear_button.pack_forget()

    def login(self):
        # Aquí debes implementar la lógica de autenticación con una base de datos de usuarios
        # Por ahora, simplemente verificaremos si el usuario ingresó un nombre de usuario y contraseña
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "password":
            self.user_authenticated = True
            self.hide_initial_elements()
            self.start_button.pack(pady=5)
            self.stop_button.pack()
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.pack(pady=5)
            self.status_label.config(text="Status: Stopped", foreground="red")
            self.show_message("Login successful", "green")
        else:
            self.show_message("Invalid username or password", "red")

    def start_auto_clicker(self):
        if not self.is_running and self.user_authenticated:
            self.is_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.status_label.config(text="Status: Running", foreground="green")
            self.timer_thread = threading.Thread(target=self.auto_clicker_loop)
            self.timer_thread.start()

    def stop_auto_clicker(self):
        if self.is_running:
            self.is_running = False
            self.stop_button.config(state=tk.DISABLED)
            self.start_button.config(state=tk.NORMAL)
            self.status_label.config(text="Status: Stopped", foreground="red")

    def auto_clicker_loop(self):
        while self.is_running:
            x = random.randint(900, 1500)
            y = random.randint(400, 800)
            pag.moveTo(x, y, 0.2)
            pag.press("win")
            time.sleep(10)

    def clear_fields(self):
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

    def show_message(self, message, color):
        message_label = ttk.Label(self.master, text=message, foreground=color)
        message_label.pack(pady=5)
        message_label.after(3000, message_label.destroy)

def main():
    root = ThemedTk(theme="equilux")
    app = AutoClickerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

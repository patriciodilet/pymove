import tkinter as tk
import pyautogui as pag
import random
import time
import threading

# Simulación de autenticación (puedes personalizar esto)
def autenticar_usuario():
    # Lógica para verificar si el usuario tiene una cuenta activa
    # Retorna True si el usuario está autenticado, False en caso contrario
    usuario_valido = True  # Cambia esto según tu lógica de autenticación
    return usuario_valido

# Función para mover el cursor
def mover_cursor():
    x = random.randint(900, 1500)
    y = random.randint(400, 800)
    pag.moveTo(x, y, 0.2)
    pag.press("win")

# Función para iniciar la ejecución de Main
def iniciar_main():
    if autenticar_usuario():
        # El usuario está autenticado, abre la ventana secundaria
        ventana_secundaria = tk.Toplevel()
        ventana_secundaria.title("Ventana de Inicio")
        boton_iniciar = tk.Button(ventana_secundaria, text="Iniciar", command=main)
        boton_iniciar.pack()
    else:
        print("Acceso denegado. Por favor, inicia sesión primero.")

def main():
    while True:
        mover_cursor()
        time.sleep(5)

# Crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("App de Automatización")

# Etiqueta y entrada para el usuario (simulación de autenticación)
etiqueta_usuario = tk.Label(ventana_principal, text="Usuario:")
entrada_usuario = tk.Entry(ventana_principal)
etiqueta_usuario.pack()
entrada_usuario.pack()

# Botón para iniciar sesión
boton_iniciar_sesion = tk.Button(ventana_principal, text="Iniciar Sesión", command=iniciar_main)
boton_iniciar_sesion.pack()

# Ejecutar la ventana principal
ventana_principal.mainloop()

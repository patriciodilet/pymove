from flask import Flask, render_template

import pyautogui as pag
import random
import time 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/iniciar_cursor', methods=['POST'])
def iniciar_cursor():
    # Lógica para iniciar la función que mueve el cursor
    # Por ejemplo, puedes llamar a la función que ya tienes:
    mover_cursor()
    return 'Función para mover el cursor iniciada'


def mover_cursor():
    while True:
        x = random.randint(900, 1500)
        y = random.randint(400, 800)
        pag.moveTo(x, y, 0.2)
        pag.press("win")
        time.sleep(10)

if __name__ == '__main__':
    app.run(debug=True, port=8080)  # Cambia el puerto según tus necesidades
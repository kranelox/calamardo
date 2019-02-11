from flask import Flask
from flask import render_template
from luces import luzApagada, luzPrendida
import RPi.GPIO as gpio           
from time import sleep

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('plantilladecontrol.html')

@app.route('/lucesOn')
def encederLuces():
    luzPrendida()

@app.route('/lucesOff')
def encederLuces():
    luzApagada()


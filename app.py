from flask import Flask
from flask import render_template
import luces 

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template("plantilladecontrol.html")

@app.route('/lucesOn')
def encederLuces():
    luces.luzPrendida()
    return render_template("plantilladecontrol.html")
    
@app.route('/lucesOff')
def apagarLuces():
    luces.luzApagada()
    return render_template("plantilladecontrol.html")

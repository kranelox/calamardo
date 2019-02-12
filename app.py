from flask import Flask
from flask import render_template
import luces 
import pepite_sensor

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

@app.route('/temperatura')
def tempe_hum():
    valores = pepite_sensor.sens_temp_hum()
    return render_template ("plantilladecontrol.html", datos=valores)
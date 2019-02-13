from flask import Flask
from flask import render_template
from flask import jsonify
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

@app.route('/ventiOn')
def encenderVenti():
    luces.ventiPrendido()
    return render_template("plantilladecontrol.html")

@app.route('/ventiOff')
def apagarVenti():
    luces.ventiApagado()
    return render_template("plantilladecontrol.html")

@app.route('/temperatura')
def tempe_hum():
    temp, hum = pepite_sensor.sens_temp_hum() #se cambia las variables para separar los valores del sensor
    valores = {"temperatura":temp, "humedad":hum} #se crea diccionario con los valores del sensor
    return jsonify(valores) #se utiliza la función jsonify de flask

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

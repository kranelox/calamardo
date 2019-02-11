from flask import flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('plantilladecontrol.html')

    if __name__ == '__main__':
        app.run(debug=True)
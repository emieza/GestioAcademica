
from flask import Flask, render_template
from models import *


flask_app = Flask(__name__)

classe = Classe()


@flask_app.route("/")
def hello():
    return render_template('hola.html', nombre="Lean")

@flask_app.route("/llistat_alumnes")
def llistat_alumnes():
    return render_template('llistat_alumnes.html',classe=classe)

@flask_app.route("/crea_alumne")
def crea_alumne():
    alumne = classe.crea_alumne()
    return render_template('crea_alumne.html',alumne=alumne)

if __name__ == "__main__":
    flask_app.run()


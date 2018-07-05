from flask import Flask, render_template
flask_app = Flask(__name__)

@flask_app.route("/")
def hello():
    return render_template('hola.html', nombre="Lean")

@flask_app.route("/llistat_alumnes")
def llistat_alumnes():
    return render_template('llistat_alumnes.html')

if __name__ == "__main__":
    flask_app.run()


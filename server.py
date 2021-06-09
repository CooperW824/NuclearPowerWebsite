from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("HomePage.html")

@app.route("/bibliography")
def bib():
    return render_template("Bibliography.html")

@app.route("/nuclear")
def nuclear():
    return render_template("NuclearPower.html")

@app.route("/thorium")
def thorium():
    return render_template("ThoriumPower.html")
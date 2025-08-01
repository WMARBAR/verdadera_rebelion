# app.py
from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')

# Renombramos la ruta y función para que sea /material_apoyo
@app.route('/material_apoyo')
def material_apoyo():
    return render_template('material_apoyo.html')

@app.route("/egyse")
def egyse():
    # “gordo y sin energía”  → e.g.  /egyse
    return render_template("egyse.html")

@app.route("/nsqctv")
def nsqctv():
    # “gordo y sin energía”  → e.g.  /nsqctv
    return render_template("nsqctv.html")

@app.route("/plf")
def plf():
    # “gordo y sin energía”  → e.g.  /plf
    return render_template("plf.html")

@app.route("/abretumente")
def abretumente():
    # “gordo y sin energía”  → e.g.  /abretumente
    return render_template("abretumente.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

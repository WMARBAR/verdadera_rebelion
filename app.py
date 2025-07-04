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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

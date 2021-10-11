from app import app
from flask import render_template, request


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/dd-calculator')
def ddcalculator():
    return render_template('calculadora.html')


@app.route('/dd-calculator', methods=['POST'])
def calculate():
    value = float(request.form['value'])
    low = 100 - value
    recovery = round(((value / low) * 100), 2)
    return render_template('calculadora.html', result=recovery)
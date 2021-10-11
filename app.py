import os
from flask import Flask,request
from flask import render_template


app = Flask(__name__)

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


#teste localhost
'''if __name__ == '__main__':
    app.run(debug=True)'''

#teste heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

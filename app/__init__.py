from flask import Flask

app = Flask(__name__)

from app import routes


app.run(debug=True, port=8080, host='192.168.15.11')
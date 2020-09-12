import socket
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    hostname = socket.gethostname()
    return render_template('home.html', hostname=hostname)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

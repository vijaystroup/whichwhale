import socket
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    hostname = socket.gethostname()
    client = request.remote_addr
    return render_template('home.html', hostname=hostname, client=client)

@app.route('/terms')
def terms():
    return render_template('terms.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

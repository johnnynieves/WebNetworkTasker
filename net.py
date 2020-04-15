from flask import Flask, redirect, render_template, url_for, request
from napalm import get_network_driver

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/credentials', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        ip = request.form['ip']
        username = request.form['username']
        password = request.form['password']
        ios = request.form['ios']
        return redirect(url_for('interfaces', ip=ip, username=username, password=password, ios=ios))

    else:
        print('YOUR MESSAGE IS A GET !!!')
    return render_template('credentials.html')


@app.route('/interfaces')
def interfaces(ip, username, password, ios):
    driver = get_network_driver(ios)
    with driver(ip, username, password) as device:
        info = device.get_interfaces()

    return info


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

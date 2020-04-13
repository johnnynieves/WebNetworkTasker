from flask import Flask, redirect, render_template, url_for, request
from napalm import get_network_driver

app = Flask(__name__)

menu = ['Get device info',
        'Get IOS Version',
        'IOS Upgrade',
        'Link status for your Device',
        'Check port-security'
        'Check Interface Names',
        'Make "Golden" Configs',
        'Verify configs against "Golden" configs',
        'quit'
        ]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/credentials', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        print('Your message is a post')
    else:
        print('Your message is a get')
    return render_template('credentials.html')


@app.route('/interfaces')
def interfaces():
    driver = get_network_driver('ios')
    with driver('10.0.0.123', 'jnieves', 'johnny', timeout=10) as device:
        info = device.get_interfaces()

    return info


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

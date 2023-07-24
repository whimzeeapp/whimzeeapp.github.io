from flask import Flask, current_app, send_file
app = Flask(__name__)

@app.route('/')
def index():
    return send_file('index.html')


@app.route('/support')
def support():
    return send_file('support.html')

@app.route('/private-policy')
def private_policy():
    return send_file('private-policy.html')

@app.route('/gallery')
def gallery():
    return send_file('gallery.html')
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Cilui Github CI\CD ;)'

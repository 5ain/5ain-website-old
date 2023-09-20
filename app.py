from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html', methods = ['GET'])

@app.route('/about')
def about():
    return render_template('about.html', methods = ['GET'])

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html', methods = ['GET'])

app.run()

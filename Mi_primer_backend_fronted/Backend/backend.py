from flask import Flask, render_template

app = Flask(__name__, template_folder='../frontend')
"""
@app.route('/')
def home():
    return "Hello world"
@app.route('/dinero')
def dinero():
    return "aqui solo hay dinero"
"""
@app.route('/')
def home():
    return render_template('frontend.html')
@app.route('/dinero')
def dinero():
    return render_template('dinero.html')
@app.route('/lenguajes')
def lenguajes():
    lenguajes = ("PHP", "JavaScript", "Python", "C#", "Rust", "Perl")
    return render_template('lenguajes.html', lenguajes=lenguajes)
if __name__ == '__main__':
    app.run(debug = True, port = 3500 )
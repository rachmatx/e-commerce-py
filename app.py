from flask import Flask, render_template, request

app = Flask(__name__)

def create_app():
    app.config['SECRET_KEY'] = 'mkasmdkwei'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True, port=8080)
from flask import Flask, request, render_template, url_for

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def pagina1():
    return render_template('index.html')
    
@app.route('/about')
def pagina2():
    return render_template('about.html')
    
@app.route('/dashboard')
def pagina3():
    return render_template('dashboard.html')
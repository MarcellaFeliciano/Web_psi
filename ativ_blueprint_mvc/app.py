from flask import Flask, render_template
from controllers import users, books, emprestimos

app = Flask(__name__)
app.register_blueprint(users.bp)
app.register_blueprint(books.bp)
app.register_blueprint(emprestimos.bp)


@app.route('/')
def index():
    return render_template('index.html')




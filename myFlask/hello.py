from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():#This handles application URLS, known as view functions, the return value is the **response** the client receives
    return '<h>Hello World!</h1>'

@app.route('/user/<name>')
def user(name):
    return f'<h>Hello, {name}!</h1>'


#app.add_url_rule('/', 'index',index)


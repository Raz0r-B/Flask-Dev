from flask import Flask
from flask import request
from flask import make_response
from flask import redirect


app = Flask(__name__)

linkTree = '''
<a href="/">Home</a>
<br>
<a href="/user/Brandon">User:Brandon</a>
<br>
<a href="/BadRequest">Bad Request</a>
<br>
<a href="/cookie">Cookies!</a>
<br>
<a href="/redirect">Leave</a>
'''


#A standard view function to url route '/'
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent') #gets the agent(browser) the user is using to access the server
    
    html=f'''
    <h1>Hello! Welcome home</h1>
    <p>Your browser is {user_agent}</p>
    <br>
    {linkTree}
    
    '''   
    return html


# A Standard view function using a user/<whateverUserName> route
@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    html=f'''
    <h1>Hello, {name}!</h1>
    <p>You are running this in {user_agent}</p>
    <br>
    {linkTree}
    '''
    return html

#A view function for a bad request
@app.route('/BadRequest')
def bad_request():
    return '<h1>Bad Request</h1><a href="/">Home</a>', 400 #returns text we want displayed to a user and a bad request code

@app.route('/cookie')
def cookie():
    html=f'''
    <h1>You get a cookie!</h1>
    <a href="/">Home</a>
    '''
    response = make_response(html)
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def goGoogle():
    return redirect('https://www.google.com')
    
    

        


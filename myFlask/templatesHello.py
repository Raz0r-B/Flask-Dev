from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask import redirect
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

#A standard view function to url route '/'
@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent') #gets the agent(browser) the user is using to access the server
    return render_template('index.html',user_agent=user_agent)


# A Standard view function using a user/<whateverUserName> route
@app.route('/user/<name>')
def user(name):
    user_agent = request.headers.get('User-Agent')
    
    return render_template('user.html',user_agent=user_agent, name=name )

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

@app.route('/variables')
def vars():
    myDict={'user':'Thrilla'}
    myList = ['I','indeed','Rock']
    myintvar = 1
    return render_template('variables.html', mydict= myDict, #first value is for template, 2nd value is for code in this program
                                            myList = myList,
                                            myintvar = myintvar)
    
    

        


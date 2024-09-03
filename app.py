from flask import Flask,render_template,request#rt-A function to render HTML templates.
from weather import main as get_weather

app = Flask(__name__)#Initializes a new Flask application. The __name__ variable helps Flask determine the root path for the application.


@app.route('/',methods=('GET','POST'))#@app.route('/', methods=('GET', 'POST')): Defines the route for the root URL (/). It accepts both GET and POST requests.
def index():
    data =None
    if request.method == 'POST':
       city  = request.form['cityname']
       state = request.form['statename']
       country = request.form['countryname']
       data = get_weather(city,state,country)
    return render_template("Indextemplate.html",data = data)


if __name__ == '__main__':
    app.run(debug = True)#Starts the Flask development server with debug mode enabled. Debug mode provides detailed error messages and automatically reloads the server when code changes.
    

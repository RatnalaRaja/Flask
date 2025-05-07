from flask import Flask,render_template
'''
It creates instancee for flask,which will be our WSGI
'''

app= Flask(__name__)

### WSGI application

@app.route("/")
def welcome():
    return "<html><H1>Hiii</h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')


if __name__=="__main__":
    app.run(debug=True)
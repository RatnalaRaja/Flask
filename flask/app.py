from flask import Flask
'''
It creates instancee for flask,which will be our WSGI
'''

app= Flask(__name__)

### WSGI application

@app.route("/")
def welcome():
    return "welcome to flask home page"

if __name__=="__main__":
    app.run(debug=True)
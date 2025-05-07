from flask import Flask,request,render_template
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

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="POST":
        name=request.form["name"]
        return f'Hello {name}'
    return render_template("form.html")



if __name__=="__main__":
    app.run(debug=True)
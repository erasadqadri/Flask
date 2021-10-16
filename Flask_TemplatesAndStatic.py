from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
    #return "<h1>Home Page</h1>"

@app.route("/asad")
def asad():
    return "<h1>Asad's Page</h1>"

if __name__== "__main__":
    app.run(debug=True)
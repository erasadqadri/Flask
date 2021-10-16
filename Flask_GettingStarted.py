from flask import Flask
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page</h1>"

@app.route("/asad")
def asad():
    return "<h1>Asad's Page</h1>"

if __name__== "__main__":
    app.run(debug=True)  #can change port by app.run(debug=True, port=8000)
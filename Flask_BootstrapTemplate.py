from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("bootstrap.html")

@app.route("/todo")
def ToDO():
    return "<h1>Asad's ToDo List</h1>"


if __name__== "__main__":
    app.run(debug=True)
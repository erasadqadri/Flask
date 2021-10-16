#For Database:
#pip install flask-sqlalchemy
#sqlalchemy is an ORM mapper

from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///Asad_Flask.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ToDo(db.Model):
    sr_no = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sr_no} - {self.title}"

@app.route("/", methods=['GET','POST'])
def home():
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']

        todo = ToDo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    alltodo = ToDo.query.all()
    print(alltodo)
    return render_template("bootstrap.html", alltodo=alltodo)

@app.route("/update")
def update():
    alltodo = ToDo.query.all()
    print(alltodo)
    return "this is all todo list"

@app.route("/delete/<int:sr_no>")
def delete(sr_no):
    todo = ToDo.query.filter_by(sr_no=sr_no).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

if __name__== "__main__":
    app.run(debug=True)
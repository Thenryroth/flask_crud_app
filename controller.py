import os
from flask import Flask
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask import redirect

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app.config["SQLALCHEMY_DATABASE_URI"] = database_file
db = SQLAlchemy(app)


class Book(db.Model):
    title = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)

    def __repr__(self):
        return "<Title: {}>".format(self.title)




@app.route("/", methods=["GET"])
def list():
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/books", methods=["POST"])
def create():
    book = Book(title=request.form.get("title"))
    db.session.add(book)
    db.session.commit()
    books = Book.query.all()
    return render_template("home.html", books=books)

@app.route("/books/<title>", methods=["GET"])
def read(title):
    book = Book.query.filter_by(title=title).first()
    return render_template("book.html", book=book)


@app.route("/update", methods=["POST"])
def update():
    newtitle = request.form.get("newtitle")
    oldtitle = request.form.get("oldtitle")
    book = Book.query.filter_by(title=oldtitle).first()
    book.title = newtitle
    """
    update db.book set book.title = {newtile} where book.title = {oldtitle}
    """
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
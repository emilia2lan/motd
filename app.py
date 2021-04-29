import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/motd'
db = SQLAlchemy(app)


#add columns in the table
class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(150), unique=True, nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='cat.jpg')

    def __repr__(self):
      return f"Name('{self.message}', '{self.image_file}'"


posts = [
    {'message': 'It makes a big difference in your life when you stay positive.'},
    {'message': 'You are off to great places, today is your day.'},
    {'message': 'Live life to the fullest and focus on the positive.'},
    {'message': 'If opportunity does not knock, build a door.'}
]

db.create_all()

# endpoint
@app.route("/", methods=["GET", "POST",])
def add_name():
    return render_template('home.html', posts=posts)


if __name__ == '__main__':
    app.run()

import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# connect to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/motd'
db = SQLAlchemy(app)

#create table and add columns
class Greets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    message = db.Column(db.String(150), unique=True, nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='cat.jpg')

    def __repr__(self):
      return f"('{self.message}', '{self.name}', '{self.image_file}')"
db.create_all()

greets = [{'name': 'Simon', 'message': 'It makes a big difference in your life when you stay positive.'}, {'name': 'Bernhard', 'message': 'You are off to great places, today is your day.'}, {'name': 'Daniela', 'message': 'Live life to the fullest and focus on the positive.'}, {'name': 'Emilia', 'message': 'If opportunity does not knock, build a door.'},
]

# endpoint
@app.route("/", methods=["GET", "POST",])
def create():
  greets_new = {'name': 'Andreas', 'message': 'When life gives you lemons make a lemonade.'}
  greets.append(greets_new)
  return jsonify( greets)
    # return render_template('home.html', greets=greets)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session, relationship

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://motd:motd@localhost/motd'
app.debug = True

db = SQLAlchemy(app)
session = Session()
# creates two tables and joins on name column

class c_names(db.Model):
  __tablename__ = 'names_t'
  name = db.Column(db.String(50), primary_key=True, nullable=False)

  def __init__(self, name):
    self.name = name

class c_greets(db.Model):
  __tablename__ = 'greets_t'
  name = db.Column(db.String(50), primary_key=True)
  message = db.Column(db.String())

  def __init__(self, name, message):
    self.name = name
    self.message = message

db.create_all()

#insert multiple values in greets_t
greets = [c_greets(name="Simon", message="Happiness is the only thing that multiplies when you share it."), c_greets(name="Bernhard", message="You are off to great places, today is your day."), c_greets(name="Daniela", message="Live life to the fullest and focus on the positive."), c_greets(name="Emilia", message="If opportunity does not knock, build a door."),c_greets(name="Cat", message="/cat.jpg")]

db.session.add_all(greets)
try:
  db.session.commit()
except:
  db.session.close()

@app.route('/names', methods=['GET'])
def names():
  allNames = c_names.query.all()
  output = []
  for name in allNames:
    newName = {}
    newName['name'] = name.name
    output.append(newName)
  return jsonify(output)

@app.route('/api/v1/greet', methods=['POST'])
def namesNew():
  namesData = request.get_json()
  newName = c_names(name=namesData['name'])
  db.session.add(newName)
  db.session.commit()
  return jsonify(namesData)


if __name__ == '__main__':
  app.run(debug=True)

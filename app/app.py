import json
import random

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Session, relationship

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://motd:motd@localhost/motd'
app.debug = True

db = SQLAlchemy(app)
session = Session()

# creates two tables
class motd(db.Model):
  __tablename__ = 'random_greeting'
  greets = db.Column(db.String(), primary_key=True)
  def __init__(self, greets):
    self.greets = greets

class u_greets(db.Model):
  __tablename__ = 'user_greeting'
  user = db.Column(db.String(), primary_key=True)
  greeting = db.Column(db.String())
  def __init__(self, user, greeting):
    self.user = user
    self.greeting = greeting

db.create_all()


#insert multiple values in the two tables
greets = [u_greets(user="Simon", greeting="Happiness is the only thing that multiplies when you share it."), u_greets(user="Bernhard", greeting="You are off to great places, today is your day."), u_greets(user="Daniela", greeting="Live life to the fullest and focus on the positive."), u_greets(user="Emilia", greeting="If opportunity does not knock, build a door."),u_greets(user="Cat", greeting="/cat.jpg")]

motd_list = [motd(greets="Welcome!"), motd(greets="How are you?"), motd(greets="Today is a good day!"), motd(greets="Nice to meet you!")]

db.session.add_all(greets)
db.session.add_all(motd_list)
try:
  db.session.commit()
except:
  db.session.close()

@app.route('/api/v1/greet', methods=['POST'])
def namesNew():
  namePost = request.get_json()
  username = namePost["user"]

#fetch all the values from user_greeting table
  allUsers = u_greets.query.all()
  output = []
  for user in allUsers:
    result = {}
    result['user'] = user.user
    result['greeting']=user.greeting
    output.append(result)

#fetch all the values from random_greeting table
  allGreets = motd.query.all()
  result2 = []
  for greets in allGreets:
    quotes = {}
    quotes['greets'] = greets.greets
    result2.append(quotes)

  # loops through user_greetings.user and check if the name inserted(post method) is in or not.
  something = {}
  for i in range(5):
    something[output[i]["user"]] = output[i]["greeting"]

  if username in something:
    return username + something[username]
    # if not returns the new user and gives a random message from random_greeting table
  else:
   return username + result2[random.randint(0, 3)]['greets']

  return json.dumps({"msg": msg}, output, something, username, separators=" ")

if __name__ == '__main__':
  app.run(debug=True)

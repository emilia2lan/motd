from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/motd'
app.debug = True

db = SQLAlchemy(app)

class c_greets(db.Model):
  __tablename__ = 'greets'
  name = db.Column(db.String(80), primary_key=True)
  message = db.Column(db.String(), nullable=False)

  def __init__(self, name, message):
    self.name = name
    self.message = message


db.create_all()


@app.route('/test', methods=['GET'])
def test():
  return {
    'test': 'test'
  }

@app.route('/greets', methods=['GET'])
def greets():
  allGreets = c_greets.query.all()
  output = []
  for greet in allGreets:
    newGreet = {}
    newGreet['name'] = greet.name
    newGreet['message'] = greet.message
    output.append(newGreet)
  return jsonify(output)

@app.route('/api/v1/greet', methods=['POST'])
def greetsNew():
  greetsData = request.get_json()
  newName = c_greets(name=greetsData['name'], message=greetsData['message'])
  db.session.add(newName)
  db.session.commit()
  return jsonify(greetsData)


if __name__ == '__main__':
  app.run(debug=True)

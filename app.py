import os

from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from sqlalchemy import create_engine

db_connect = create_engine('postgresql://postgres:postgres@localhost/motd')
app = Flask(__name__)

# access the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/motd'
api = Api(app)

class Greets(Resource):
    def get(self):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select * from greets") # query and returns json result
        return {'msg': [i[0] for i in query.cursor.fetchall()]} # fetches first column

    def post(self):
        conn = db_connect.connect()
        print(request.json)
        # to do: fix the typeError
        name = request.json['name']
        message = request.json['message']
        query = conn.execute("insert into greets values(null,'{0}','{1}')".format(name, message))
        return {'status':'success'}


# endpoint
api.add_resource(Greets, '/v1/greets')

if __name__ == '__main__':
  app.run(debug=True)

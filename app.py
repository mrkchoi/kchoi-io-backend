from flask import Flask, request
from flask_cors import CORS
import main

app = Flask(__name__)

CORS(app)

@app.post('/api/data')
def create_query():
  request_data = request.get_json()
  query_string = request_data['query']  
  response = main.ask_bot(query_string)
  return {'data': response}, 201

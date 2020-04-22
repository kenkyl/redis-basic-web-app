from flask import Flask, request, jsonify
from flask_cors import CORS
import redis

# REDIS SETUP
redis_host = 'localhost'
redis_port = 6379
r = redis.StrictRedis(redis_host, redis_port, charset="utf-8", decode_responses=True)

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/players/<int:player_id>', methods=['POST', 'PUT', 'GET'])
def players_handler(player_id):
    if (request.method == 'GET'):
        player = r.hgetall(f'players:{player_id}')
        return player, 200, {'Content-Type':'application/json'}
    elif (request.method == 'PUT'):
        player = request.get_json()
        pid = player.get('id')
        result = r.hmset(f'players:{player_id}', player)
        print(f'received player with id {pid}. updated with result {result}')
        return player, 200, {'Content-Type':'application/json'}
    return 'players endpoint'
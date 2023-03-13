
from uuid import uuid4
from flask import Flask, request, jsonify
import datetime
import json
import hashlib
import urllib.parse as url
import requests

app = Flask(__name__)

class Blockchain(object):

    def __init__(self):
        self.chain = []
        self.nodes = set()
        self.new_block("genesis block", "temp", 0)

    def new_block(self, client, data, previous_hash):
        temp = {
            'client': client,
            'data': data,
        }
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(datetime.datetime.now()),
            'information': temp,
            'previous_hash': previous_hash #placing the next prev hash into the current block
        }
        self.chain.append(block)

        return block

    @property
    def previous_block(self):
        return self.chain[-1]

    @staticmethod
    def hash_block(block):
        serialized_block = json.dumps(block, sort_keys=True).encode()

        return hashlib.sha256(serialized_block).hexdigest()
        
blockchain = Blockchain()
miner_address = str(uuid4())

@app.route('/input', methods=['POST'])
def create_transaction():
    transaction = request.get_json()

    required_keys = ['client', 'data']

    if not all(key in transaction for key in required_keys):
        return 'Invalid keys in request.', 400
    previous_hash = blockchain.hash_block(blockchain.previous_block)
    block = blockchain.new_block(transaction['client'], transaction['data'], previous_hash)

    response = {
        'message': 'Data uploaded',
        'index': block['index'],
        'timestamp': block['timestamp'],
        'information': block['information'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 201

@app.route('/blocks', methods=['GET'])
def read_blocks():
    blocks = {
        'message': 'This is the current chain',
        'blockchain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(blocks), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

from flask import Flask, jsonify
from bitcoinlib.wallets import Wallet

app = Flask(__name__)

def get_balance(address):
    wallet = Wallet()
    balance = wallet.get_balance(address)
    return balance

@app.route('/balance/<address>', methods=['GET'])
def balance(address):
    balance = get_balance(address)
    return jsonify({'address': address, 'balance': balance})

import requests

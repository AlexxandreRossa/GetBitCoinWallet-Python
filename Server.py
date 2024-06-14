import requests
import json
import xmlrpc.server

def get_bitcoin_balance(account):
    api_url = f"https://blockcShain.info/balance?active={account}"

    try:
        response = requests.get(api_url)
        data = response.json()
        balance = data[account]['final_balance'] / 100000000
        return balance
    except Exception as e:
        print("Erro ao consultar saldo da conta Bitcoin:", e)
        return None


server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))
server.register_function(get_bitcoin_balance, "get_balance")


print("Servidor RPC iniciado em localhost:8000...")
server.serve_forever()

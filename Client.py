import xmlrpc.client

def get_balance_from_server(account):
    proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")
    bitcoin_balance = proxy.get_balance(account)
    return bitcoin_balance

account = "3FXuhCd2rXhFSDca5hzQ5qdZYK4z42z2RS"
balance = get_balance_from_server(account)
print(f"Saldo da conta {account}: {balance} BTC")

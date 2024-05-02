import requests

def get_balance(address):
    url = f'http://localhost:5000/balance/{address}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == '__main__':
    address = input("Insira o endereço da conta Bitcoin: ")
    balance_data = get_balance(address)
    print(f"Saldo da conta {balance_data['address']}: {balance_data['balance']}")

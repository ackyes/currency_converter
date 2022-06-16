from pkgutil import extend_path
import requests

currency_code_map = {
    "btc": "Bitcoin",
    "usd": "United States dollar",
    "krw": "South Korean won",
    "eur": "Euro",
    "etc": "Ethereum Classic",
    "doge": "Dogecoin",
    "jpy": "Japanese yen",
    "vnd": "Vietnamese dong",
}

# API Call function
url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
response = requests.get(url_host)
sample_json = response.json()

def get_exchange_rate(from_code, to_code):
    url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/"
    endpoint = from_code + "/" + to_code
    ext = ".json"
    url = url_host + endpoint + ext
    response = requests.get(url)
    if response.ok:
        exchange = response.json()
        rate = exchange[to_code]
    else:
        rate = 0
    return response.ok, rate

def get_currencies(currency_code_map):
    #set empty string
    currency_string = []

    #get the 3 -letter code and currency from currency map
    for code in currency_code_map.keys():
        str = currency_code_map[code]
        currency_string.append(code + " - " + str)
    return currency_string

def get_currency_from_code(code):
    return currency_code_map[code]

def get_currency_string(code):
    return code + "-" + get_currency_from_code(code)

currencies = get_currencies(currency_code_map)
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")

if __name__ == "__main__":
    get_currencies(currency_code_map)
    success, rate = get_exchange_rate("usd", "eur")
    print(rate)
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

def get_currencies():
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
    return code + " - " + get_currency_from_code(code)

# API Call function
url_host = "https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies.min.json"
response = requests.get(url_host)
currency_code_map = response.json()

currencies = get_currencies()
default_from = get_currency_string("usd")
default_to = get_currency_string("eur")

if __name__ == "__main__":
    get_currencies()
    print(get_currency_string())
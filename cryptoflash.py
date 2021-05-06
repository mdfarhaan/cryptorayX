import requests
from currency_converter import CurrencyConverter

url = "https://api.wazirx.com/api/v2/tickers"
response = dict(requests.get(url).json())

class cryptoflash :

    def price(self,coin,currency):
        try:
            currencyObject = CurrencyConverter()
            
            crypto = coin.lower() + "inr"
            currentPrice = float(response[crypto]["last"])
            try:
                price = currencyObject.convert(currentPrice, 'INR', currency.upper(),)
                print(price)
            except ValueError:
                print(currency + " is invalid.")
        
        except KeyError:
            print(coin + " is invalid.")


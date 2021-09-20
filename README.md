# Crypto Flash
#### Crypto Flash is a Lightweight Python module to get Crypto currency prices
##### This module uses the WazirX Public API


# Usage
### The ```cryptoflash``` module can be installed using pip
```python
pip install cryptoflash
```
### Import ```cryptoflash``` module
```python
from cryptoflash import cryptoflash
```
### Create an Object:

```python
coin = cryptoflash()
```
### Get Price:
Set the **Coin** and **Currency** as an argument by calling the ```price()``` function.
```python
btc_price = coin.price("BTC", "INR")
print(btc_price)
```
> NOTE: Both the Coin and Currency argument takes in the value in the form
of symbol respectively.

#### Your all up and ready to roll!!

**- MdFarhaan**

# Crypto Flash
#### Crypto Flash is a Lightweight Python module to get Crypto currency prices


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
Set the **Coin** and **Currency** by calling the ```price()``` function.
It takes two argument that is the _Coin_ and _Currency_
```python
btc_price = coin.price("BTC", "INR")
print(btc_price)
```
> NOTE: Both the Coin and Currency argument takes in the value in the form
of symbol.

#### Your all up and ready to roll!!

**- MdFarhaan**

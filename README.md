# alipay_sdk_django

## Get APPID and three keys from alipay

1. register a developer goto [open alipay platform](https://openhome.alipay.com/platform/appDaily.htm)  and get your APPID 
2. download RSAkeyMaker from https://docs.open.alipay.com/291/105971 and you will get two keys divide save as `app_public_key2048.txt` and `app_private_key2048.txt`
3. backto  [open alipay platform](https://openhome.alipay.com/platform/appDaily.htm) copy `self_public_key2048.txt`  to  RSA2(SHA256)setting get third key save as `alipay_public_key.txt` 

## Alipay network

Alipay APi ：https://openapi.alipay.com/gateway.do 

| API list                                                     | type | descripe                   |
| ------------------------------------------------------------ | ---- | ---------------------- |
| [alipay.trade.fastpay.refund.query](https://docs.open.alipay.com/api_1/alipay.trade.fastpay.refund.query) | free | query for trade and refund |
| [alipay.trade.order.settle](https://docs.open.alipay.com/api_1/alipay.trade.order.settle) | free | api for order settle   |
| [alipay.trade.close](https://docs.open.alipay.com/api_1/alipay.trade.close) | free | api for close   |
| [alipay.trade.cancel](https://docs.open.alipay.com/api_1/alipay.trade.cancel) | free | api for cancel   |
| [alipay.trade.refund](https://docs.open.alipay.com/api_1/alipay.trade.refund) | free | api for refund   |
| [alipay.trade.precreate](https://docs.open.alipay.com/api_1/alipay.trade.precreate) | free | precreate trade |
| [alipay.trade.create](https://docs.open.alipay.com/api_1/alipay.trade.create) | free | api for trade create |
| [alipay.trade.pay](https://docs.open.alipay.com/api_1/alipay.trade.pay) | free | api for trade pay  |
| [alipay.trade.query](https://docs.open.alipay.com/api_1/alipay.trade.query) | free | query for trade   |
| [koubei.trade.itemorder.query](https://docs.open.alipay.com/api_1/koubei.trade.itemorder.query) | free | query for itemorder |
| [koubei.trade.itemorder.buy](https://docs.open.alipay.com/api_1/koubei.trade.itemorder.buy) | free | api for itemorder buy   |
| [koubei.trade.itemorder.refund](https://docs.open.alipay.com/api_1/koubei.trade.itemorder.refund) | free | api for itemorder refund   |
| [alipay.fund.auth.order.freeze](https://docs.open.alipay.com/api_1/alipay.fund.auth.order.freeze) | free | api for order freeze       |
| [alipay.trade.app.pay](https://docs.open.alipay.com/api_1/alipay.trade.app.pay) | free | api for app pay  |
| [alipay.trade.wap.pay](https://docs.open.alipay.com/api_1/alipay.trade.wap.pay) | free | api for wap pay  |
| [koubei.trade.ticket.ticketcode.send](https://docs.open.alipay.com/api_1/koubei.trade.ticket.ticketcode.send) | free | api for ticketcode send    |
| [koubei.trade.ticket.ticketcode.delay](https://docs.open.alipay.com/api_1/koubei.trade.ticket.ticketcode.delay) | free | api for ticketcode delay        |
| [koubei.trade.ticket.ticketcode.cancel](https://docs.open.alipay.com/api_1/koubei.trade.ticket.ticketcode.cancel) | free | api for ticketcode cancel      |
| [koubei.trade.ticket.ticketcode.query](https://docs.open.alipay.com/api_1/koubei.trade.ticket.ticketcode.query) | free | query for ticketcode     |
| [alipay.trade.orderinfo.sync](https://docs.open.alipay.com/api_1/alipay.trade.orderinfo.sync) | free | apifor orderinfo sync |

## Example

### 1. Requirements

```python
pip install pycryptodome
```

windows need `pip install winrandom` from https://www.lfd.uci.edu/~gohlke/pythonlibs/#winrandom

###2. create a class named Alipay for alipay api

```python
class AliPay(object):
    def __init__(self, appid, app_notify_url, app_private_key_path,
                 alipay_public_key_path, return_url, debug=False):
        self.appid = appid
        self.app_notify_url = app_notify_url
        self.app_private_key_path = app_private_key_path
        self.app_private_key = None
        self.return_url = return_url
        with open(self.app_private_key_path) as fp:
            self.app_private_key = RSA.importKey(fp.read())
        self.alipay_public_key_path = alipay_public_key_path
        with open(self.alipay_public_key_path) as fp:
            self.alipay_public_key = RSA.importKey(fp.read())
        if debug is True:
            self.__gateway = "https://openapi.alipaydev.com/gateway.do"
        else:
            self.__gateway = "https://openapi.alipay.com/gateway.do"
```

### 3. create an instance

```python
alipay = AliPay(
    appid="2016091300503105",
    app_notify_url="http://127.0.0.1:8000/alipay/return",
    app_private_key_path="../trade/keys/app_private_key2048.txt",
    alipay_public_key_path="../trade/keys/alipay_public_key.txt",  
    debug=True,  # 默认False,
    return_url="http://118.190.202.67:8000/"
)
```








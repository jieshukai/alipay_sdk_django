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

### 2. create an instance

```python
alipay = AliPay(
    appid="2016091300503105", # your appid
    app_notify_url="http://127.0.0.1:8000", # your web api
    app_private_key_path="app_private_key2048.txt", 
    alipay_public_key_path="alipay_public_key.txt",  
    debug=True,  # for dev 
    return_url="http://127.0.0.1:8000/"
)
```

###3.  generate  url 

```python
url = alipay.direct_pay(
    subject='subject', 
    out_trade_no='{}'.format(time.strftime('%Y%m%d%H%M%S')),  # time stamp
    total_amount=888 
)
re_url = "https://openapi.alipaydev.com/gateway.do?{data}".format(data=url)
print(re_url)
```








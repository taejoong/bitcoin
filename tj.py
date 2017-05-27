import requests
import json

bitstamp = requests.get("https://www.bitstamp.net/api/v2/ticker/btcusd/")
b = json.loads(bitstamp.text)
bitstamp = b['last']

#print bitstamp

coinone = requests.get("https://coinone.co.kr/json/recent_trades/btc/")
c = json.loads(coinone.text)
coinone =  c['trade_list'][-1]['price']

exchange_rate = requests.get('http://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20yahoo.finance.xchange%20where%20pair%20in%20(%22USDKRW%22)&format=json&env=store://datatables.org/alltableswithkeys&callback=')
exchange_rate = float(json.loads(exchange_rate.text)['query']['results']['rate']['Rate'])

margin = 1.035

volume = 15000

coin_buy = volume / ( float(bitstamp) * margin ) 
won_sell = coin_buy * float(coinone)

print "coin-one: %s, bitstamp: %s" % (coinone, bitstamp)
#print coin_buy
#print won_sell
selling_price = won_sell / exchange_rate
profit = selling_price - volume

print "selling_price: %s, profit: %s" % (selling_price, profit)
#print selling_price
#print profit

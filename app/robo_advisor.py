
import json
import requests
import os
from dotenv import load_dotenv
import datetime
import pandas as pd 

import csv

def dollar_format(input):
	return "${0:,.2f}".format(input)


#getting the api key form the .env file
#but don't want to upload .env to the repository
API_KEY = os.environ.get("MY_API_KEY")
load_dotenv()

#https://stackoverflow.com/questions/19486369/extract-csv-file-specific-columns-to-list-in-python
colnames = ['code', 'name']
filename = "digital_currency_list.csv"
data = pd.read_csv(filename,names=colnames)

currency_symbols = data.code.tolist()
currency_names = data.name.tolist()

while True:
	try:
		print("What symbol would you like to check? Enter 'S' to see the accepted symbols!")
		request_symbol = str(input())
		#https://stackoverflow.com/questions/9257094/how-to-change-a-string-into-uppercase
		#takes user input to upper case 
		request_symbol = request_symbol.upper()
		if(request_symbol == 'S'):
			for symbol in currency_symbols: print(" +" + symbol)
				

			raise Exception

		elif(request_symbol not in currency_symbols):
			print("Not in the accepted cryptocurrencies symbol list, please try again. ")
			raise Exception 
		break
	except:
		pass


request_url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=" + request_symbol + "&market=USD&apikey=" + "&apikey="
request_url = request_url + str(API_KEY)








# or could do
# request_url = f"url={API_KEY}"


response = requests.get(request_url)

print("Status: " + str(response.status_code))
#print("Response text: " + str())


parsed_response = json.loads(response.text)

#print(parsed_response)

#parsed_response["Time Series(Daily)"]["2019-02-18"]["4. close"]

dict_list = []

#dict_list = parsed_response["Time Series (Digital Currency Daily)"]
#print(dict_list)
#print("Latest closing price is: " + response.text)





#output
print("*******************************************")
print("Cryptocurrency selected: " + request_symbol)
#https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
current_time = datetime.datetime.now()
#https://stackabuse.com/how-to-format-dates-in-python/
current_time = current_time.strftime("%b %d %Y %H:%M")
current_time = str(current_time)
print("Request Sent: " + current_time)

print("Latest Refreshed: " + parsed_response["Meta Data"]["6. Last Refreshed"])

print("*******************************************")


#adapted from Prof Rossetti's solution

list_keys = []
list_keys = list(parsed_response["Time Series (Digital Currency Daily)"].keys())

print(len(list_keys))
latest_open = parsed_response["Time Series (Digital Currency Daily)"][list_keys[0]]["1a. open (USD)"]
latest_high = parsed_response["Time Series (Digital Currency Daily)"][list_keys[0]]["2a. high (USD)"]
latest_low = parsed_response["Time Series (Digital Currency Daily)"][list_keys[0]]["3a. low (USD)"]
latest_close = parsed_response["Time Series (Digital Currency Daily)"][list_keys[0]]["4a. close (USD)"]
latest_volume = parsed_response["Time Series (Digital Currency Daily)"][list_keys[0]]["5. volume"]
latest_market_cap = parsed_response["Time Series (Digital Currency Daily)"][list_keys[0]]["6. market cap (USD)"]


latest_open = dollar_format(float(latest_open))
latest_high = dollar_format(float(latest_high))
latest_low = dollar_format(float(latest_low))
latest_close = dollar_format(float(latest_close))
latest_market_cap = dollar_format(float(latest_market_cap))
#https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
latest_volume = "{0:.2f}".format(float(latest_volume))


high_price_list = []
low_price_list = []

counter = 0
for dates in list_keys:
	if(counter < 100):
		high_price_list.append(parsed_response["Time Series (Digital Currency Daily)"][dates]["2a. high (USD)"])
		low_price_list.append(parsed_response["Time Series (Digital Currency Daily)"][dates]["3a. low (USD)"])
		counter = counter+1
		print(counter)

recent_high_price = max(high_price_list)
recent_high_price = dollar_format(float(recent_high_price))

recent_low_price = min(low_price_list)
recent_low_price = dollar_format(float(recent_low_price))





print("Latest Open: " + str(latest_open))
print("Latest High: " + str(latest_high))
print("Latest Low: " + str(latest_low))
print("Latest Close: " + str(latest_close))
print("Latest Volume: " + str(latest_volume))
print("Latest Market Cap: " + latest_market_cap)
print("Recent High Price: " + str(recent_high_price))
print("Recent Low Price: " + str(recent_low_price))





#http://blog.appliedinformaticsinc.com/how-to-parse-and-convert-json-to-csv-using-python/
# open a file for writing


#data_csv = open('data/prices.csv', 'w')

# create the csv writer object

parsed_response = parsed_response["Time Series (Digital Currency Daily)"]
print("****************")
#print(parsed_response)
print("*****************")
#csvwriter = csv.writer(parsed_response)



count = 0

#for parsed in parsed_response:


#      csvwriter.writerow(parsed.text())

#data_csv.close()








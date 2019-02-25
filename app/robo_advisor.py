
import json
import requests
import os
from dotenv import load_dotenv


import os
import pandas as pd 




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
		if(request_symbol == 'S'):
			for symbol in currency_symbols: print(" +" + symbol)
				

			raise Exception

		elif(request_symbol not in currency_symbols):
			print("Not in the accepted cryptocurrencies symbol list, please try again. ")
			raise Exception 
		break
	except:
		pass



request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + request_symbol + "&apikey="
request_url = request_url + str(API_KEY)








# or could do
# request_url = f"url={API_KEY}"


response = requests.get(request_url)

print("Status: " + str(response.status_code))
#print("Response text: " + str())

parsed_response = json.loads(response.text)

#parsed_response["Time Series(Daily)"]["2019-02-18"]["4. close"]



print("Latest closing price is: " + response.text)



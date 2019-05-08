
import json
import requests
import os
from dotenv import load_dotenv
import datetime
import pandas as pd 
import sys
import csv
import pprint

from robo_advisor_revisited import dollar_format, compile_url, get_response, transform_response, write_to_csv



#getting the api key form the .env file
#but don't want to upload .env to the repository
load_dotenv()
API_KEY = os.environ.get("API_KEY")


#print(API_KEY)


#https://stackoverflow.com/questions/19486369/extract-csv-file-specific-columns-to-list-in-python
colnames = ['code', 'name']

try:	
	filename = "digital_currency_list.csv"
	data = pd.read_csv(filename,names=colnames)
except:
	sys.exit("The digital_currency_list.csv file is not in the same directory as this script. Please download from https://www.alphavantage.co/digital_currency_list/ and try again.")

currency_symbols = data.code.tolist()
currency_names = data.name.tolist()

print("Welcome to Graham's Robo Adivsor! This python script will help you choose a cryptocurrency stock to pick.")

parsed_response_list = []
request_symbol_list = []
list_keys_list = []
counter = 0

data_response_dict = {'1':{},'2':{},'3':{}}


while counter < 3:
	counter = counter + 1
	while True:
		try:
			while True:
				try:
					print("What symbol (3) would you like to check? Enter 'S' to see the accepted symbols!")
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



			#revisited
			request_url = compile_url(request_symbol,API_KEY)
			print(request_url)
			#revisited
			parsed_response = get_response(request_url)

			request_symbol_list.append(request_symbol)
			break


		except:

			print("Sorry, the API does not have data on that cryptocurrency. Please try again.")
			pass
	parsed_response_list.append(parsed_response)

symbol_counter = 0
for parsed in parsed_response_list:
	#output
	print("*******************************************")
	print("Cryptocurrency selected: " + request_symbol_list[symbol_counter])
	symbol_counter = symbol_counter + 1
	#https://stackoverflow.com/questions/415511/how-to-get-the-current-time-in-python
	current_time = datetime.datetime.now()
	#https://stackabuse.com/how-to-format-dates-in-python/
	current_time = current_time.strftime("%b %d %Y %H:%M")
	current_time = str(current_time)
	print("Request Sent: " + current_time)

	
	print("Latest Refreshed: " + parsed["Meta Data"]["6. Last Refreshed"])

	print("*******************************************")



	#adapted from Prof Rossetti's solution

	list_keys = []
	list_keys = list(parsed["Time Series (Digital Currency Daily)"].keys())
	list_keys_list.append(list_keys)



	#revisited
	#gets the requested data
	data_response = transform_response(list_keys, parsed)

	#sets nested list of results
	data_response_dict[symbol_counter] = data_response


	high_price_list = []
	low_price_list = []

	#gets recent high and low
	counter = 0
	for item in data_response_dict[symbol_counter]['high'].items():
		#gets value from the tuple
		value = item[1]
		high_price_list.append(value)
	for item in data_response_dict[symbol_counter]['low'].items():
		value = item[1]
		low_price_list.append(value)

			


	recent_high_price = max(high_price_list)
	recent_high_price = dollar_format(float(recent_high_price))

	recent_low_price = min(low_price_list)
	recent_low_price = dollar_format(float(recent_low_price))





	print("Latest Open: " + dollar_format(float(data_response_dict[symbol_counter]['open'][0])))
	print("Latest High: " + dollar_format(float(data_response_dict[symbol_counter]['high'][0])))
	print("Latest Low: " + dollar_format(float(data_response_dict[symbol_counter]['low'][0])))
	print("Latest Close: " + dollar_format(float(data_response_dict[symbol_counter]['close'][0])))
	print("Latest Volume: " + ("{0:,.2f}".format(float(data_response_dict[symbol_counter]['volume'][0]))))
	print("Latest Market Cap: " + ("{0:,.2f}".format(float(data_response_dict[symbol_counter]['market_cap'][0]))))
	print("Recent High Price: " + str(recent_high_price))
	print("Recent Low Price: " + str(recent_low_price))



write_to_csv(data_response_dict,request_symbol_list)


symbol_counter = 0



iterator = 1
for i in range(3):

	#algorithm for recommendation
	volume1 = 0
	volume2 = 0
	volume3 = 0
	increasing_volume = False
	volume_percent_change = 0
	volume_percent_change_is_desired = False
	increasing_price = False



	volume1 = data_response_dict[iterator]['volume'][0]
	volume2 = data_response_dict[iterator]['volume'][1]
	volume3 = data_response_dict[iterator]['volume'][2]

	price1 = data_response_dict[iterator]['high'][0]
	price2 = data_response_dict[iterator]['high'][1]
	price3 = data_response_dict[iterator]['high'][2]

	iterator = iterator +1



	volume_percent_change = (volume1 - volume2)/volume1

	if(volume1 > volume2 and volume2 > volume3):
		increasing_volume = True

		if(volume_percent_change > .25):
			volume_percent_change_is_desired = True



	if(price1 > price2 and price2 > price3):
		increasing_price = True
	print("")
	print("")

	if(increasing_volume == True and volume_percent_change_is_desired == True and increasing_price == True):
		print("You should buy! The conditions have been satisified!")
		print("This algorithm bases crypto currency buy choices off the concept of momentum")
		print(request_symbol_list[symbol_counter] + " has had an increasing price and significant increase in volume of trade.")
		print("Therefore, this currency has upward momentum and the user should buy.")
	else:
		print("You should not buy " + request_symbol_list[symbol_counter])
		print(request_symbol_list[symbol_counter] + " did not fulfill the requirements to have upward momentum")

	symbol_counter = symbol_counter + 1

	print("*******************************************")
	print("*******************************************")









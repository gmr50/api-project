import json
import requests
import pandas as pd
import datetime
import csv

def dollar_format(input):


	result = "${0:,.2f}".format(input)


	return result


def compile_url(request_symbol, API_KEY):

	request_url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=" + request_symbol + "&market=USD&apikey=" + "&apikey="
	request_url = request_url + str(API_KEY)

	return request_url



def get_response(request_url):
	#https://stackoverflow.com/questions/543309/programmatically-stop-execution-of-python-script/543375
	try:
		response = requests.get(request_url)
		parsed_response = json.loads(response.text)
	except:
		sys.exit("Something went wrong with the API! Check your internet connection and try again!")


	#some of the symbols listed in the digital_currency_list.csv don't work. 
	#https://stackoverflow.com/questions/1602934/check-if-a-given-key-already-exists-in-a-dictionary
	if 'Error Message' in parsed_response:
		raise Exception


	return parsed_response



def transform_response(list_keys, parsed):

	response_list = []
	latest_open_list = []
	high_list = []
	low_list = []
	close_list = []
	volume_list =[]
	market_cap_list = []
	date_list = []
	
	counter = 0

	for index,dates in enumerate(list_keys):

		if(index==100):
			break
		else:
			latest_open = parsed["Time Series (Digital Currency Daily)"][dates]["1a. open (USD)"]
			#latest_open = dollar_format(float(latest_open))
			latest_open_list.append(latest_open)


			latest_high = parsed["Time Series (Digital Currency Daily)"][dates]["2a. high (USD)"]
			#latest_high = dollar_format(float(latest_high))
			high_list.append(latest_high)

			latest_low = parsed["Time Series (Digital Currency Daily)"][dates]["3a. low (USD)"]
			#latest_low = dollar_format(float(latest_low))
			low_list.append(latest_low)

			latest_close = parsed["Time Series (Digital Currency Daily)"][dates]["4a. close (USD)"]
			#latest_close = dollar_format(float(latest_close))
			close_list.append(latest_close)

			latest_volume = parsed["Time Series (Digital Currency Daily)"][dates]["5. volume"]
			latest_volume = float(latest_volume)
			#latest_volume = "{0:,.2f}".format(float(latest_volume))
			volume_list.append(latest_volume)

			latest_market_cap = parsed["Time Series (Digital Currency Daily)"][dates]["6. market cap (USD)"]
			#latest_market_cap = "{0:,.2f}".format(float(latest_market_cap))
			latest_market_cap = float(latest_market_cap)
			market_cap_list.append(latest_market_cap)

			date_list.append(dates)


	response_dataframe = pd.DataFrame(data = {'open': latest_open_list, 
	'high': high_list, 
	'low': low_list, 
	'close': close_list, 
	'volume': volume_list, 
	'market_cap': market_cap_list,
	'date': date_list} )

	response_dict = response_dataframe.to_dict()


	return response_dict




def write_to_csv(response_dict, request_symbol_list):

	
	datestring = datetime.datetime.now().today().strftime(' %m %d %y  ')
	datestring1 = datetime.datetime.now().time().strftime('%H %M %S')
	filename = getcwd() + '/data/prices' + datestring + datestring1 + '.csv'

	#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/csv.md
	with open(filename, 'w') as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=["crypto", "timestamp", "open", "high", "low", "close", "volume", "market cap"])
		writer.writeheader()
		symbol_counter = 0
		counter = 1

		for i in range(3):
			writer.writerow({"crypto": request_symbol_list[symbol_counter]})
			

			#gets length of dictionary
			dictionary_length = len(response_dict[1]['open'])

			for iterator in range(dictionary_length):
				writer.writerow({
					"timestamp": response_dict[counter]['date'][iterator],
					"open": (dollar_format(float(response_dict[counter]['open'][iterator]))),
					"high": (dollar_format(float(response_dict[counter]['high'][iterator]))),
					"low": (dollar_format(float(response_dict[counter]['low'][iterator]))),
					"close": (dollar_format(float(response_dict[counter]['close'][iterator]))),
					"volume": ("{0:,.2f}".format(float(response_dict[counter]['volume'][iterator]))),
					"market cap": ("{0:,.2f}".format(float(response_dict[counter]['market_cap'][iterator])))

					})
			counter = counter + 1
			symbol_counter = symbol_counter + 1

	return filename







if __name__ == "__main__":
    print("main")
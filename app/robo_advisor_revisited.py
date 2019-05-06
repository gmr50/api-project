import json
import requests
import pandas as pd

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


	# response_dataframe = pd.DataFrame(columns = ['latest_open','latest_high', 'latest_low', 'latest_close', 'latest_volume', 'latest_market_cap'])

	# for dates in list_keys:
	# 	item = parsed["Time Series (Digital Currency Daily)"][dates]["1a. open (USD)"]
	# 	item = dollar_format(float(item))
	# 	response_dataframe['latest_open'].append(item)

	# print("response dataframe")
	# print(response_dataframe)
	
	counter = 0



	
	for index,dates in enumerate(list_keys):

		if(index==100):
			break
		else:
			latest_open = parsed["Time Series (Digital Currency Daily)"][dates]["1a. open (USD)"]
			latest_open = dollar_format(float(latest_open))
			latest_open_list.append(latest_open)


			latest_high = parsed["Time Series (Digital Currency Daily)"][dates]["2a. high (USD)"]
			latest_high = dollar_format(float(latest_high))
			high_list.append(latest_high)

			latest_low = parsed["Time Series (Digital Currency Daily)"][dates]["3a. low (USD)"]
			latest_low = dollar_format(float(latest_low))
			low_list.append(latest_low)

			latest_close = parsed["Time Series (Digital Currency Daily)"][dates]["4a. close (USD)"]
			latest_close = dollar_format(float(latest_close))
			close_list.append(latest_close)

			latest_volume = parsed["Time Series (Digital Currency Daily)"][dates]["5. volume"]
			latest_volume = "{0:.2f}".format(float(latest_volume))
			volume_list.append(latest_volume)

			latest_market_cap = parsed["Time Series (Digital Currency Daily)"][dates]["6. market cap (USD)"]
			latest_market_cap = dollar_format(float(latest_market_cap))
			market_cap_list.append(latest_market_cap)




	response_dataframe = pd.DataFrame(data = {'open': latest_open_list, 
	'high': high_list, 
	'low': low_list, 
	'close': close_list, 
	'volume': volume_list, 
	'market_cap': market_cap_list } )


	return response_dataframe




def write_to_csv():

	counter = 0
	#https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/notes/python/modules/csv.md
	with open('data/prices.csv', 'w') as csv_file:
		writer = csv.DictWriter(csv_file, fieldnames=["crypto", "timestamp", "open", "high", "low", "close", "volume", "market cap"])
		writer.writeheader()
		symbol_counter = 0

		for parsed2 in parsed_response_list:
			writer.writerow({"crypto": request_symbol_list[symbol_counter]})
			symbol_counter = symbol_counter + 1
			for lists in list_keys_list:
				for dates in lists:

					if(counter < 100):
						counter = counter + 1
						writer.writerow({"timestamp": dates, 
						"open": parsed2["Time Series (Digital Currency Daily)"][dates]["1a. open (USD)"],
						"high": parsed2["Time Series (Digital Currency Daily)"][dates]["2a. high (USD)"],
						"low": parsed2["Time Series (Digital Currency Daily)"][dates]["3a. low (USD)"],
						"close": parsed2["Time Series (Digital Currency Daily)"][dates]["4a. close (USD)"],
						"volume": parsed2["Time Series (Digital Currency Daily)"][dates]["5. volume"],
						"market cap": parsed2["Time Series (Digital Currency Daily)"][dates]["6. market cap (USD)"]})
			counter = 0
	# uses fieldnames set above
	# create the csv writer object






if __name__ == "__main__":
    print("main")
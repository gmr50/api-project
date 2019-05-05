

def dollar_format(input):


	result = "${0:,.2f}".format(input)


	return result


def compile_url(request_symbol, API_KEY):

	request_url = "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=" + request_symbol + "&market=USD&apikey=" + "&apikey="
	request_url = request_url + str(API_KEY)

	return request_url





if __name__ == "__main__":
    print("main")
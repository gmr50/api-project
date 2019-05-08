from robo_advisor_revisited import dollar_format, compile_url, transform_response


def test_dollar_format():

	test_passed = False
	input = 10000
	result = dollar_format(input)



	if(result[0] == '$' and result[3] == ',' and result[-1] == '0' and result[-2] == '0'):
		test_passed = True


	assert test_passed == True

	#reset for next test
	#testing now with trailing decimals
	test_passed = False

	result = dollar_format(10.99999999)

	if(result == "$11.00"):
		test_passed = True

	assert test_passed == True

	#reset for next test
	#testing with fewer decimals

	test_passed = False
	result = dollar_format(1.1)
	if(result == "$1.10"):
		test_passed = True

	assert test_passed == True


def test_compile_url():

	result = compile_url("TEST","TEST")
	assert result == "https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=TEST&market=USD&apikey=&apikey=TEST"




def test_transform_response():


	test_dict = {
	"Meta Data": {
		"1. Information": "Daily Prices and Volumes for Digital Currency",
		"2. Digital Currency Code": "TEST",
		"3. Digital Currency Name": "TEST-DICT",
		"4. Market Code": "USD",
		"5. Market Name": "United States Dollar",
		"6. Last Refreshed": "2019-05-07 (end of day)",
		"7. Time Zone": "UTC"
	},
	"Time Series (Digital Currency Daily)": {
		"2019-05-07": {
			"1a. open (USD)": "1",
			"1b. open (USD)": "2",
			"2a. high (USD)": "3",
			"2b. high (USD)": "4",
			"3a. low (USD)": "5",
			"3b. low (USD)": "6",
			"4a. close (USD)": "7",
			"4b. close (USD)": "8",
			"5. volume": "9",
			"6. market cap (USD)": "10"
			}
		}
	}
	list_keys = list(test_dict["Time Series (Digital Currency Daily)"].keys())



	data_response = transform_response(list_keys,test_dict)

	assert data_response['open'][0] == "1"
	assert data_response['high'][0] == "3"
	assert data_response['low'][0] == "5"
	assert data_response['close'][0] == "7"
	assert data_response['volume'][0] == 9.0
	assert data_response['market_cap'][0] == 10.0
	assert data_response['date'][0] == "2019-05-07"





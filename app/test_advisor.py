from robo_advisor_revisited import dollar_format, compile_url, transform_response, write_to_csv
import csv
import os

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
			},
		"2019-05-06": {
			"1a. open (USD)": "200",
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
	assert data_response['open'][1] == "200"




def test_write_to_csv():

	request_symbol_list = ['test1', 'test2', 'test3']

	test_dict = {1: {'close': {0: '100',
			   1: '200',
			   },
	 'date': {0: '300',
			  1: '400',
			  },
	 'high': {0: '500',
			  1: '600',
			  },
	 'low': {0: '700',
			 1: '800',
			},
	 'market_cap': {0: 10.1,
					1: 10.2,
					},
	 'open': {0: '900',
			  1: '1000',
			  },
	 'volume': {0: 10.3,
				1: 10.4,
				}},

	2: {'close': {0: '100',
			   1: '200',
			   },
	 'date': {0: '300',
			  1: '400',
			  },
	 'high': {0: '500',
			  1: '600',
			  },
	 'low': {0: '700',
			 1: '800',
			},
	 'market_cap': {0: 10.1,
					1: 10.2,
					},
	 'open': {0: '900',
			  1: '1000',
			  },
	 'volume': {0: 10.3,
				1: 10.4,
				}},

	3: {'close': {0: '100',
			   1: '200',
			   },
	 'date': {0: '300',
			  1: '400',
			  },
	 'high': {0: '500',
			  1: '600',
			  },
	 'low': {0: '700',
			 1: '800',
			},
	 'market_cap': {0: 10.1,
					1: 10.2,
					},
	 'open': {0: '900',
			  1: '1000',
			  },
	 'volume': {0: 10.3,
				1: 10.4,
				}}


	}


	


	filename = write_to_csv(test_dict,request_symbol_list)
	#filename = (os.getcwd()) + '/' + filename


	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		rows = [r for r in csv_reader]

		assert rows[1][0] == 'test1'
		assert rows[2][1:8] == ["300","$900.00","$500.00","$700.00","$100.00","10.30","10.10"]
		assert rows[3][1:8] == ["400","$1,000.00","$600.00","$800.00","$200.00","10.40","10.20"]
		assert rows[4][0] == 'test2'
		assert rows[5][1:8] == ["300","$900.00","$500.00","$700.00","$100.00","10.30","10.10"]
		assert rows[6][1:8] == ["400","$1,000.00","$600.00","$800.00","$200.00","10.40","10.20"]
		assert rows[7][0] == 'test3'
		assert rows[8][1:8] == ["300","$900.00","$500.00","$700.00","$100.00","10.30","10.10"]
		assert rows[9][1:8] == ["400","$1,000.00","$600.00","$800.00","$200.00","10.40","10.20"]

	os.remove(filename)

	
	










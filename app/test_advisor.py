from robo_advisor_revisited import dollar_format, compile_url


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


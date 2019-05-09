# robo-advisor

Hello! Thanks for using my robo advisors. In order for the software to work, a few requirements need to be met:
	+Install requirements: pip install -r requirements.txt
	+A data directory on level up from the directory the python script is in (/data/)
	+The digital_currency_list.csv must be in the same directory as the python script. It can be found at https://www.alphavantage.co/digital_currency_list/
		It must be named 'digital_currency_list.csv'

Despite the alphavantage.co claiming "The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list.", that is not true and some of the cryptocurrencies will not work! For testing purposes, keep with well known currencies such as BTC, ETH, LTC.

Finally, your api key should be held in a file called api_key_new_key.env and set your key to a variable named API_KEY

For the multi_robo_advisor, it accepts 3 currency symbols. Again, BTC, ETH, ETC, LTC all work for this purpose. 

Revisitation updates have been done to multi_robo_advisor.py, new functions within robo_advisor_revisited.py

Test using pytest
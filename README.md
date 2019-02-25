# robo-advisor

Hello! Thanks for using my robo advisors. In order for the software to work, a few requirements need to be met:
	+The following environments should be installed in your environment: json, os, requests, dotenv, datetime, pandas, sys, csv
	+A data directory on level up from the directory the python script is in (/data/)
	+The digital_currency_list.csv must be in the same directory as the python script. It can be found at https://www.alphavantage.co/digital_currency_list/
		It must be named 'digital_currency_list.csv'

Despite the alphavantage.co claiming "The digital/crypto currency of your choice. It can be any of the currencies in the digital currency list.", that is not true and some of the cryptocurrencies will not work! For testing purposes, keep with well known currencies such as BTC, ETH, LTC.



For the multi_robo_advisor, it accepts 3 currency symbols. Again, BTC, ETH, ETC, LTC all work for this purpose. 
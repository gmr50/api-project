
import json
import requests
import os
from dotenv import load_dotenv

#KUJH9GJWRGFXNJBW"

#getting the api key form the .env file
#but don't want to upload .env to the repository
API_KEY = os.environ.get("MY_API_KEY")
load_dotenv()


request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=GOOG&apikey="
request_url = request_url + str(API_KEY)


# or could do
# request_url = f"url={API_KEY}"


response = requests.get(request_url)

print("Status: " + str(response.status_code))
#print("Response text: " + str())

parsed_response = json.loads(response.text)

#parsed_response["Time Series(Daily)"]["2019-02-18"]["4. close"]



print("Latest closing price is: " + response.text)



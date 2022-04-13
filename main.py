import requests
from datetime import date, timedelta
from twilio.rest import Client
TO = '##########'

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_API_KEY = '########################'
STOCK_API_KEY = '######################'

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_API_KEY = '#############################'
TWILIO_SID = '############################'
TWILIO_PHONE = '+#############'

client = Client(TWILIO_SID, TWILIO_API_KEY)
# STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# HINT 1: Get the closing price for yesterday and the day before yesterday.
# Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
# HINT 2: Work out the value of 5% of yerstday's closing stock price.
stock_json = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': STOCK_API_KEY
}
stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_json)
tsla_data = stock_response.json()
today = date.today()
yesterday = today - timedelta(days=1)
today = today.strftime('%Y-%m-%d')
yesterday = yesterday.strftime('%Y-%m-%d')





# STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
# HINT 1: Think about using the Python Slice Operator
news_params = {
    'apikey': NEWS_API_KEY,
    'q': STOCK,
    'searchIn': 'title,description',
    'language': 'es',
    'sortBy': 'popularity'
}

news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
articles = news_response.json()['articles']
# print(articles[0])
if float(tsla_data['Time Series (Daily)'][today]['4. close']) < \
        1.1*float(tsla_data['Time Series (Daily)'][yesterday]['4. close']):
    message = f"{STOCK} ha subido más de 5 % ⬆, puede deberse a : \n "
    for article in articles:
        message = message + article['title'] + "\n"
        message = message + article['description'] + "\n"
        message += article['url']
        send_message = client.messages \
            .create(
            body=message,
            from_=TWILIO_PHONE,
            to=TO
        )

# print(message)
# STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
# HINT 1: Consider using a List Comprehension.




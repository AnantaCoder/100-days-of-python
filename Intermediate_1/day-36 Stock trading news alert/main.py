import requests
from datetime import datetime, timedelta

STOCK_NAME = "TSLA"
STOCK_API_KEY = 'ILBMA95DJ77IMS4G'
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "77feaab553924ec2ab8eba7ad3ade19b"


TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"

# STEP 1: Use the Daily Time Series API
stock_url = f"{STOCK_ENDPOINT}?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}"
r = requests.get(stock_url)
data = r.json()

# Get yesterday's and the day before's date in the format YYYY-MM-DD
yesterday = (datetime.now() - timedelta(2)).strftime('%Y-%m-%d')
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday = (datetime.now() - timedelta(3)).strftime('%Y-%m-%d')

print(f'Tesla stock Price from {day_before_yesterday} to {yesterday}')

# Get yesterday's and the day before yesterday's closing stock prices
try:
    yesterday_close = float(data["Time Series (Daily)"][yesterday]["4. close"])
    day_before_yesterday_close = float(data["Time Series (Daily)"][day_before_yesterday]["4. close"])
    
    # print(f"Yesterday's Closing Price: {yesterday_close}")
    # print(f"Day Before Yesterday's Closing Price: {day_before_yesterday_close}")

    
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
    price_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) * 100

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
    #printing the peice change 
    
    if price_change > 0:
        up= "📈"
        print(f"The stock price of Tesla is {up}{up}{up} by {abs(price_change):.2f} % ")
    else:
        down = "📉"
        print(f"The stock price of Tesla is {down}{down}{down} by {abs(price_change):.2f} % ")
except KeyError:
    print("Data for the requested dates is not available yet.")



#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
# news_url = (f'{NEWS_ENDPOINT}?''sources=bbc-news&'
#             f'apiKey={NEWS_API_KEY}')
# news_date = requests.get(news_url)
# news_data = news_date.json()
# for articles in news_data['articles']:
#     if articles['source']['name'] == 'BBC News':
#         print(articles['title'])
#         print(articles['description'])

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
parameters = {
    'q': 'Tesla',          
    'apiKey': NEWS_API_KEY,      
    'sortBy': 'publishedAt', 
    'language': 'en',       
    'pageSize': 5            
}
articles_list = []
response = requests.get(NEWS_ENDPOINT, params=parameters)
if response.status_code == 200:
    data = response.json()
    articles = data.get('articles', []) # fetck the article list 
    if articles:
        for i, article in enumerate(articles[:3]):
            print(f"Title: {article['title']}")
            articles_list.append(article['title'])
            print(f"Description: {article['description']}")
            print(f"URL: {article['url']}")
            print("-" * 50)
    else:
        print("No articles found for Tesla.")
else:
    ("Failed to fetch the data ")
    
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
print(articles_list[:2])



    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


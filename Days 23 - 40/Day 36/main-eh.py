import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY = '4d9353ad2ffd4d7b9c9c05779e9901ff'
API_ENDPOINT = 'https://newsapi.org/v2/everything'
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
API_KEY_STOCK = "XI6FTONX5CE8O7NA"
news_params = {
    "q": "tesla stock",
    'apiKey': API_KEY
} 
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_STOCK

}


## STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value)  in stock_data.items()]

yesterday_data = float(stock_data_list[0]["4. close"])
db_yesterday_data = float(stock_data_list[1]["4. close"])

difference = abs(yesterday_data - db_yesterday_data)
diff_percent = round(((difference / yesterday_data) * 100), 2)


# ---------------------------------------------------------------------------------------------------------------------------------

## STEP 2: Use https://www.alphavantage.co
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

def get_news():
    news_request = requests.get(API_ENDPOINT, params=news_params)
    news_request.raise_for_status()
    news_data = news_request.json()
    three_articles = news_data["articles"][:3]
    formatted_articles = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    for item in formatted_articles:
        print(item, "\n")


#  BONUS PART: MAKE THE PROGRAM TO WORK INTERCONNECTED.


if diff_percent >= 0.5:
    print(f"{diff_percent}, SELL THE STOCKS!!!\n")
    get_news()
else:
    print(f"{diff_percent} percent, It is all right.")


import time
from crypto_api import CryptoAPI
from web_scraper import WebScraper
from data import API_KEY, TICKER
#import boto3
import twitter_tweepy




crypto_api = CryptoAPI(api_key=API_KEY, symbol=TICKER)
scraper = WebScraper(symbol=TICKER, crypto_api=crypto_api)




def find_difference_in_price(new : float, old : float) -> dict:
    '''
    Calculate the difference between two numbers in percent and float values

    Parameters
    ----------
    new : float
        the 'current' num
    old : float
        the 'previous' num
    
    Returns
    -------
    dict
        a dictionary containing the difference in percent format and float format
    '''
    percent = ((new - old) / old) * 100 # percent change between two nums
    difference = "{:.2f}".format((new - old))
    return {"percent": percent, "difference": difference}

def tweet() -> None:
    '''
    Handle making a tweet

    Returns
    -------
    None
    '''
    media_location = "./canvas.png"
    crypto_dict = crypto_api.get_price()
    current_price = crypto_dict['current_price']
    price_1hour_ago = crypto_dict['price_60min']

    hour1 = find_difference_in_price(current_price, price_1hour_ago)
    
    print(f"1h Price is up/down: {hour1['percent']:.2f}%")
    
    
    # if stock is down more than 0.50%
    if hour1['percent'] < -0.50:
        scraper.screenshot_stock_graph(filename="canvas", hours_24=False)
        message = f"#{crypto_api.digital_currency_name} is DOWN {hour1['percent']:.2f}% in the last hour! \nCurrent: ${current_price} \nLast hour: ${price_1hour_ago} \nChange: ${hour1['difference']}"
        twitter_tweepy.send_tweet(message=message, media_location="./canvas.png")
        print(message)
        return

    
    # # if stock is up in the last hour, find the price it was 24hours ago
    if hour1['percent'] > 0:
        price_24hours_ago = crypto_api.get_price_24hours_ago().get('price')
        hour24 = find_difference_in_price(current_price, price_24hours_ago)
        print(f"24h Price is up/down: {hour24['percent']:.2f}%")
        
        # if stock was up in the last 24 hours
        if hour24["percent"] > 0 and hour24["percent"] > 1.5:
            scraper.screenshot_stock_graph(filename="canvas", hours_24=True)

            # format 2 decimal places - example: 0.0345 = 3.45
            message = f"#{crypto_api.digital_currency_name} is UP {hour24['percent']:.2f}% in the last 24 hours! \nCurrent: ${current_price} \nLast 24hours: ${price_24hours_ago} \nChange: ${hour24['difference']}"
            twitter_tweepy.send_tweet(message=message, media_location=media_location)
            print(message)
            return
        
        # if stock was down more than 2.50% in the last 24 hours
        if hour24["percent"] < -2.50:
            scraper.screenshot_stock_graph(filename="canvas", hours_24=True)
            message = f"#{crypto_api.digital_currency_name} is DOWN {hour24['percent']:.2f}% in the last 24 hours! \n Current: ${current_price} \n Last 24hours: ${price_24hours_ago} \n Change: ${hour24['difference']}" # format 2 decimal places - example: 0.0345 = 3.45
            
            # send tweet
            twitter_tweepy.send_tweet(message=message, media_location=media_location) 
            print(message)
            return
    else:
        print("Price is down, but not low enough to do anything. Exiting program...")
            




def main():
    tweet()
    # s3 = boto3.resource('s3')
    # object = s3.Object("dva-c01-coursebucket", 'canvas.png')
    # object.put(Body=open("./canvas.png", "rb"))

if __name__ == "__main__":
    start = time.perf_counter()
    main()
    print(f"Program took {time.perf_counter() - start} seconds to run")
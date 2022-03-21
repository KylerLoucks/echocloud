import requests

# ALPHA VANTAGE API CALL

class CryptoAPI():
    '''
    Create an object to make API calls to Alpha Vantage
    '''
    def __init__(self, api_key: str, symbol: str) -> None:
        self.symbol=symbol
        self.api_key=api_key
        self.digital_currency_name=self._handle_api_call(f"https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={self.symbol}&market=USD&interval=1min&outputsize=compact&apikey={self.api_key}")['Meta Data']['3. Digital Currency Name']
        
    
    def get_symbol_full(self) -> str:
        ''' 
        Translate the symbol to its full name 
        (BTC becomes 'Bitcoin')

        Returns
        -------
        str
            a string of the full cryptocurrency name
        '''
        return str(self.digital_currency_name)

    def _handle_api_call(self, url: str) -> dict:
        '''
        Catch errors in an API call to the specified URL
        
        Parameters
        ----------
        url : str
            The URL for the API call

        Returns
        -------
        dict
            a dictionary containing data gathered from the api call in json format
        '''
        r = requests.get(url)
        data = r.json()
        
        if not data:
            raise ValueError('Error getting data from the api, no return was given.')
        elif "Error Message" in data:
            raise ValueError(data["Error Message"])
        elif "Information" in data:
            raise ValueError(data["Information"])
        elif "Note" in data:
            print("Made too many API calls. Yikes...")
            raise ValueError(data["Note"])
        return data
    
    def get_price_24hours_ago(self) -> dict:
        '''
        Returns
        -------
        dict
            A dictionary containing the price and date a cryptocurrency was 24 hours ago
        '''
        intraday_url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={self.symbol}&market=USD&interval=60min&outputsize=compact&apikey={self.api_key}'

        data = self._handle_api_call(intraday_url)

        values = list(data.values())[1] # [1] = dictionary of 'Time Series Crypto (60min)': {}
        date = list(values.keys())[24] # grab the 'date' key 24 iterations prior
        price = float(values[f'{date}']['4. close']) # grab the highest price value from the 'date' key
        
        dict = {'date': date, 'price': price}
        return dict


    def get_price(self) -> dict:
        '''
        Returns
        -------
        dict
            a dictionary containing the prices and dates a cryptocurrency is currently, and 60 minutes ago
        '''
        intraday_url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={self.symbol}&market=USD&interval=1min&outputsize=compact&apikey={self.api_key}'

        data = self._handle_api_call(intraday_url)

        dict = list(data.values())[1] # [1] = dictionary of 'Time Series Crypto (1min)': {}
        current_date = list(dict.keys())[0] # grab the 'date' key of 'current' time
        current_price = float(dict[f'{current_date}']['4. close']) # grab the price value from the 'date' key
        
        date_60min = list(dict.keys())[60] # grab the 'date' key 60 iterations prior
        price_60min = float(dict[f'{date_60min}']['4. close']) # grab the price value from the 'date' key

        return {'current_date': current_date, 'current_price': current_price, "date_60min": date_60min, "price_60min": price_60min}


    # def get_highest_price_day(self, interval: int = 0) -> dict:
    #     '''
    #     Get the highest price a cryptocurrency was during a prior day
    #     interval: number of days prior to current date - Default: 0
    #     '''
    #     daily_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={self.symbol}&market=USD&apikey={self.api_key}'

    #     if interval < 0:
    #         interval = 0

    #     data = self._handle_api_call(daily_url)

    #     values = list(data.values())[1] # [1] = dictionary of 'Time Series Crypto (5min)': {}
    #     date = list(values.keys())[interval] # grab the 'date' key
        
    #     highest_price = float(values[f'{date}']['2b. high (USD)']) # grab the highest price value from the 'date' key
        
    #     dict = {'date': date, 'price': highest_price}
    #     return dict





    # def get_day_start_price(self) -> dict:
    #     '''
    #     Get the price a cryptocurrency was at the start (7:00 AM UTC)
    #     '''
    #     intraday_url = f'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol={self.symbol}&market=USD&interval=60min&outputsize=compact&apikey={self.api_key}'

    #     json_response = self._handle_api_call(intraday_url)

    #     values = list(json_response.values())[1] # [1] = dictionary of 'Time Series Crypto (5min)': {}
        
    #     current_date = datetime.now().strftime("%Y-%m-%d")

    #     parsed_date = f"{current_date} 07:00:00"

    #     price = float(values[f'{parsed_date}']['4. close']) # grab the price value from the 'date' key
        
    #     dict = {'date': parsed_date, 'price': price}
    #     return dict

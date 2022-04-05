# echocloud
Posts twitter updates when Bitcoin or another specified Cryptocurrency is down a specific threshold.


# How it works
Runs a headless chromium browser in a light-weight alpine-linux Docker container environment to take a screenshot of a stock graph and post to Twitter.

Utilizes Alpha Vantage API for stock data

Container will not run continuously. It is recommended to run the container as a CRON job.

Twitter post example:
![image](https://user-images.githubusercontent.com/60449948/161397790-fd968587-51f0-4b5c-a7b5-45c2cfa540ef.png)

# Environment variables

`BLOCKCHAIN_SYMBOL`

Optional variable to specify the ticker symbol to find the stock price of (e.g. BTC, ETH, etc..)
If it is not specified, then the default symbol of 'BTC' will be used.

`AV_API_KEY`

Required API Key for Alpha Vantage stock market data


`TWITTER_API_KEY`,
`TWITTER_API_SECRET`

Required twitter API keys, which can be generated in the Twitter API developer portal under: Keys and Secrets > Consumer Keys
![image](https://user-images.githubusercontent.com/60449948/161392837-4e1c9a5b-5f97-4805-bc7c-0813905c4177.png)


`TWITTER_ACCESS_TOKEN`,
`TWITTER_ACCESS_TOKEN_SECRET`


Required twitter API keys, which can be generated in the Twitter API developer portal under: Keys and Secrets > Authentication Tokens
![image](https://user-images.githubusercontent.com/60449948/161392560-526f8d60-edbb-44e2-926f-f558363f13ca.png)


#### Building and running the container locally (replace 'key' with API key values)
  
```bash
docker build -t echocloud .

docker run -d \
-e AV_API_KEY=key \
-e TWITTER_API_KEY=key \
-e TWITTER_API_SECRET=key \
-e TWITTER_ACCESS_TOKEN=key \
-e TWITTER_ACCESS_TOKEN_SECRET=key \
-e BLOCKCHAIN_SYMBOL=ETH \
echocloud
```
  
  



  
 

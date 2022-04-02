# echocloud
Posts twitter updates when Bitcoin is down a specific threshold.


# How it works
Runs a headless chromium browser in a light-weight alpine-linux Docker container environment.



# Environment variables

###### <optional>
`BLOCKCHAIN_SYMBOL`

specify the ticker symbol to find the stock price of (e.g. BTC, ETH, etc..)


`AV_API_KEY`

API Key for Alpha Vantage stock market data

  
###### Twitter API "Consumer Keys"
`TWITTER_API_KEY`,
`TWITTER_API_SECRET`

Generated in the Twitter API developer portal under: Keys and Secrets > Consumer Keys
![image](https://user-images.githubusercontent.com/60449948/161392837-4e1c9a5b-5f97-4805-bc7c-0813905c4177.png)


###### Twitter API "Authentication Tokens"
`TWITTER_ACCESS_TOKEN`,
`TWITTER_ACCESS_TOKEN_SECRET`

Generated in the Twitter API developer portal under: Keys and Secrets > Authentication Tokens
![image](https://user-images.githubusercontent.com/60449948/161392560-526f8d60-edbb-44e2-926f-f558363f13ca.png)


###### Building and running the container locally (replace 'key' with API key values)
  
```bash
docker build -t echocloud .

docker run -d -e AV_API_KEY=key -e TWITTER_API_KEY=key -e TWITTER_API_SECRET=key -e TWITTER_ACCESS_TOKEN=key -e TWITTER_ACCESS_TOKEN_SECRET=key  -e BLOCKCHAIN_SYMBOL=BTC echocloud
```
  
  
  
  
 

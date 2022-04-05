from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from crypto_api import CryptoAPI

class WebScraper():
    '''
    Scrape for a stock graph based on the stock symbol entered
    '''

    def __init__(self, symbol: str, crypto_api: CryptoAPI) -> None:
        self.symbol = symbol
        self.symbol_full = crypto_api.get_symbol_full().lower()

    def screenshot_stock_graph(self, filename: str, hours_24: bool = False) -> None:
        '''
        Parameters
        ----------
        filename : str 
            The name of the screenshot taken in .png format
        hours_24 : bool
            True = take screenshot of a 24hour graph. False = take screenshot of 1hour graph

        Returns
        -------
        None
        '''
        options = Options()
        options.add_argument('--headless') # no browser pop-up - Remove this line when testing locally
        options.add_argument("--single-process")
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--window-size=1280x1696") # required for selenium 'execute_script()'
        options.add_argument("--disable-dev-tools")
        options.add_argument("--no-zygote")
        options.add_argument("--disable-gpu")
        options.add_argument('--start-maximized')
        options.binary_location = '/usr/bin/chromium-browser'


        print("Attempting to open headless chrome browser...")
        driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver', options=options)
        driver.get(f"https://www.coindesk.com/price/{self.symbol_full}/") # open browser
        print("Opened headless chrome browser")
        
        # switch to candles view
        driver.find_element(By.CLASS_NAME, "react-switch ").click()
        print("Switched graph to candles view")

        # remove unwanted elements
        remove_highcharts_script = """
        var highcharts = document.querySelector(".highcharts-credits");
        highcharts.parentNode.removeChild(highcharts);
        """
        remove_watermark_script = """
        var images = document.getElementsByTagName('image');
        var l = images.length;
        for (var i = 0; i < l; i++) {
            images[i].parentNode.removeChild(images[i]);
        }
        """
        
        driver.execute_script(remove_watermark_script) # remove watermark
        driver.execute_script(remove_highcharts_script) # remove highcharts.com text
        print("Removed unnecessary elements")

        if hours_24 == False:
            WebDriverWait(driver=driver, timeout=5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "highcharts-series-group")))
            driver.find_element(By.CSS_SELECTOR, "div.ibARTa:nth-child(1)").click() # click '1H' Button
            time.sleep(2) # wait for new graph to load
        
        try:
            # wait until element is visible before screenshotting
            WebDriverWait(driver=driver, timeout=5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "highcharts-series-group")))
            graph = driver.find_element(By.CSS_SELECTOR, ".price-chartstyles__PriceChartWrapper-sc-1lyescv-0")
            graph.screenshot(f"./{filename}.png")
            
            if hours_24:
                print("Screenshot created of 24h chart")
            else:
                print("Screenshot created of 1h chart")
            
            driver.close()
        except:
            raise Exception("Took too long to load the appropriate element for screenshot")

        
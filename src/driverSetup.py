from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def setupChromeDriver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument('--headless')

    return webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

driver = setupChromeDriver()
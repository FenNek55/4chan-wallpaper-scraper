from bs4 import BeautifulSoup
from driverSetup import setupChromeDriver

url = "https://boards.4chan.org/wg/catalog"
f = open("log.txt", "w+", encoding="utf-8")

driver = setupChromeDriver()
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

threadTags = soup.select(".thread")

for thread in threadTags:
    output = ""
    title = thread.select_one(".teaser b")
    meta = thread.select_one(".meta")

    numberOfResponses = meta.select_one("b")

    if title is not None:
        output += str(title.text)
    else:
        output += "NO_TITLE"
    
    output += " Number of replies: " + str(numberOfResponses.text)

    f.write(output + "\n")

f.close()


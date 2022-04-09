from driverSetup import setupChromeDriver
from bs4 import BeautifulSoup

def getThreads(url):
    driver = setupChromeDriver()
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    threadTagList = soup.select(".thread")

    parsedThreads = []

    for threadTag in threadTagList:
        threadDict = {
            "title": "",
            "numberOfResponses": 0,
            "threadLink": ""
        }

        titleTag = threadTag.select_one(".teaser b")
        teaserTag = threadTag.select_one(".teaser")
        metaTag = threadTag.select_one(".meta")
        numberOfResponsesTag = metaTag.select_one("b")

        if titleTag is not None:
            threadDict["title"] = str(titleTag.text)
        else:
            threadDict["title"] = str(teaserTag.text)[0: 20] + "..."

        threadDict["numberOfResponses"] = int(numberOfResponsesTag.text)

        parsedThreads.append(threadDict)

    return parsedThreads


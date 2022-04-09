from driverSetup import setupChromeDriver
from bs4 import BeautifulSoup
import re

def getThreads(url):
    driver = setupChromeDriver()
    driver.get(url + "/catalog")

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
        threadLinkTag = threadTag.select_one("a")

        threadId = re.findall("[0-9]+" ,str(threadLinkTag['href']))[-1]

        if titleTag is not None:
            threadDict["title"] = str(titleTag.text)
        else:
            threadDict["title"] = str(teaserTag.text)[0: 20] + "..."

        threadDict["numberOfResponses"] = int(numberOfResponsesTag.text)
        threadDict["threadLink"] = f'{url}/thread/{threadId}'

        parsedThreads.append(threadDict)

    return parsedThreads


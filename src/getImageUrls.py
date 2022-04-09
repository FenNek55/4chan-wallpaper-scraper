from driverSetup import driver
from bs4 import BeautifulSoup

def getImageUrlsFromThread(threadUrl):
    driver.get(threadUrl)
    html = driver.page_source

    soup = BeautifulSoup(html, "html.parser")
    thumbnailsTagList = soup.select("a.fileThumb")

    imageUrls = []

    for thumbnailTag in thumbnailsTagList:
        imageUrl = f"https:{str(thumbnailTag['href'])}"
        imageUrls.append(imageUrl)

    return imageUrls




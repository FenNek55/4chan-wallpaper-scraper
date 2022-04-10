import requests
from getImageUrls import getImageUrlsFromThread
import os
import shutil

def saveImageLocally(url, fileName):
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        f = open(fileName, "wb")
        f.write(res.content)
        f.close()

def saveImagesFromThread(folderPath, threadObject, numberOfImages):
    imageUrls = getImageUrlsFromThread(threadObject["threadLink"])[0: numberOfImages]
    
    if os.path.exists(folderPath):
        shutil.rmtree(folderPath, ignore_errors=True)

    os.makedirs(folderPath)

    for imageIndex, imageUrl in enumerate(imageUrls):
        filePath = f'{folderPath}/{str(imageIndex)}.jpg'
        saveImageLocally(imageUrl, filePath)
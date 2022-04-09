from getThreads import getThreads
from getImageUrls import getImageUrlsFromThread
from saveImageLocally import saveImageLocally
import os
import shutil

url = "https://boards.4chan.org/wg"
f = open("./output/threads.txt", "w+", encoding="utf-8")

threads = getThreads(url)
sortedThreads = sorted(threads, key=lambda d: d["numberOfResponses"], reverse=True)

for thread in sortedThreads:
    output = f'{thread["title"]}\nNumber of replies: {thread["numberOfResponses"]}\nLink: {thread["threadLink"]}\n\n'
    f.write(output + "\n")
f.close()

for threadIndex, thread in enumerate(sortedThreads[0: 3]):
    imageUrls = getImageUrlsFromThread(thread["threadLink"])[0: 10]
    folderPath = f'./output/{threadIndex}'

    if os.path.exists(folderPath):
        shutil.rmtree(folderPath, ignore_errors=True)

    os.makedirs(folderPath)

    for imageIndex, imageUrl in enumerate(imageUrls):
        imagePath = f'./output/{threadIndex}/{str(threadIndex) + str(imageIndex)}.jpg'

        saveImageLocally(imageUrl, imagePath)


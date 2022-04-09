from getThreads import getThreads
from getImageUrls import getImageUrlsFromThread
from saveImageLocally import saveImageLocally
import os
import sys
import shutil

args = [int(arg) for arg in sys.argv[1:]]

url = "https://boards.4chan.org/wg"

if os.path.exists("./output"):
    shutil.rmtree("./output", ignore_errors=True)

os.makedirs("./output")

f = open("./output/threads.txt", "w+", encoding="utf-8")

threads = getThreads(url)
sortedThreads = sorted(threads, key=lambda d: d["numberOfResponses"], reverse=True)

for thread in sortedThreads:
    output = f'{thread["title"]}\nNumber of replies: {thread["numberOfResponses"]}\nLink: {thread["threadLink"]}\n\n'
    f.write(output + "\n")
f.close()

for threadIndex, thread in enumerate(sortedThreads[0: args[0]]):
    imageUrls = getImageUrlsFromThread(thread["threadLink"])[0: args[1]]
    folderPath = f'./output/{threadIndex}'

    if os.path.exists(folderPath):
        shutil.rmtree(folderPath, ignore_errors=True)

    os.makedirs(folderPath)

    for imageIndex, imageUrl in enumerate(imageUrls):
        imagePath = f'./output/{threadIndex}/{str(threadIndex) + str(imageIndex)}.jpg'

        saveImageLocally(imageUrl, imagePath)


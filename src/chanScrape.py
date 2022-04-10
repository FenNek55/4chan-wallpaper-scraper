from getThreads import getThreads
from saveImageLocally import saveImagesFromThread
from threading import Thread
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

threads = []
for threadIndex, thread in enumerate(sortedThreads[0: args[0]]):
    threads.append(Thread(target=saveImagesFromThread, args=(f'./output/{threadIndex}/', thread, args[1])))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
    
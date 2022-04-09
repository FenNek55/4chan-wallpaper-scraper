from getThreads import getThreads
from getImages import getImagesUrls

url = "https://boards.4chan.org/wg"
f = open("./output/threads.txt", "w+", encoding="utf-8")

threads = getThreads(url)
sortedThreads = sorted(threads, key=lambda d: d["numberOfResponses"], reverse=True)

for thread in sortedThreads:
    output = f'{thread["title"]}\nNumber of replies: {thread["numberOfResponses"]}\nLink: {thread["threadLink"]}\n\n'
    f.write(output + "\n")
f.close()

for thread in sortedThreads[0: 3]:
    print(getImagesUrls(thread["threadLink"]))


from getThreads import getThreads

url = "https://boards.4chan.org/wg/catalog"
f = open("./output/threads.txt", "w+", encoding="utf-8")

threads = getThreads(url)

for thread in threads:
    output = f'{thread["title"]} Number of replies: {thread["numberOfResponses"]}'
    f.write(output + "\n")

f.close()


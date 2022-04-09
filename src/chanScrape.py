from getThreads import getThreads

url = "https://boards.4chan.org/wg"
f = open("./output/threads.txt", "w+", encoding="utf-8")

threads = getThreads(url)

for thread in threads:
    output = f'{thread["title"]}\nNumber of replies: {thread["numberOfResponses"]}\nLink: {thread["threadLink"]}\n\n'
    f.write(output + "\n")

f.close()


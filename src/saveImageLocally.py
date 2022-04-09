import requests

def saveImageLocally(url, fileName):
    res = requests.get(url, stream = True)

    if res.status_code == 200:
        f = open(fileName, "wb")
        f.write(res.content)
        f.close()

    return False
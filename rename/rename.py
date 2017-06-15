import urllib.request

#urllib.request.urlretrieve("https://static.hentaicdn.com/hentai/15743/1/hcdn0002.jpg", "local-filename.jpg")

url = "http://pururin.us/assets/images/data/14435/"
fileformat = ".jpg"
filePrefix = ""
lower = 1
upper = 32

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

for i in range(lower, upper+1):
    if i//10 == 0:
        filename = filePrefix+str(i) + fileformat
    else:
        filename = filePrefix+str(i) + fileformat
    link = url + filename

    req = urllib.request.Request(
        link,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
        }
    )
    result = urllib.request.urlopen(req).read()
    f = open("./HanaYoriTsubomi/"+str(i)+".jpg","wb")
    f.write(result)
    f.close();
    print("done: "+link)


print("done")

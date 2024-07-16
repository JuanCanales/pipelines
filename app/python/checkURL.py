
def getURLResponse(url):
    response = requests.get(url)
    print (response.status_code)


getURLResponse("http://www.google.com")

import urllib.request

def downloadBook(url, file_name):
    urllib.request.urlretrieve(url, file_name)
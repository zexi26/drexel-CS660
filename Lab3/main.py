import requests


def downloadFile(fileName):
    response = requests.get("http://www.gutenberg.org/files/2600/2600-0.txt")
    with open(fileName, 'wb') as f:
        f.write(response.content)


if __name__ == "__main__":
    downloadFile("sampleBook.txt")

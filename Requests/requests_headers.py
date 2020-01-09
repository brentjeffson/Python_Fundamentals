import requests


if __name__ == '__main__':
    resp = requests.get('https://mangakakalot.com/search/i_became_the')

    if resp.ok:
        print("Requests: OK")
        print("Response Code: " + str(resp.status_code))
        print("Request Amount(content): " + str(len(resp.content)))
        print("Request Amount(text): " + str(len(resp.text)))
        print("Response Headers: ")
        print(resp.headers)
        print("Request Headers: ")
        print(resp.request.headers)

        print(type(resp.headers['content-type']))
        print(resp.headers['content-type'])
        print('text/html' in resp.headers['Content-Type'])

import requests

class HttpRequester:

    def get_feed(url : str):
        response = requests.get(url)

        if response.status_code == 200:
            xml_content = response.text
            print(xml_content)
        else:
            print(f'Error {response.status_code}')



if __name__ == '__main__':
    HttpRequester.get_feed('https://rss.nytimes.com/services/xml/rss/nyt/Business.xml')

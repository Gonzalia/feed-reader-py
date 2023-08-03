import requests


class HttpRequester:

    def get_feed(url: str):
        xml_content = ""

        try:
            response = requests.get(url)
        except Exception as e:
            print(f'An error has occurred: {response.status_code}\n {e}')

        if response.status_code == 200:
            xml_content = response.text

        return xml_content


if __name__ == '__main__':

    print(HttpRequester.get_feed(
        'https://rss.nytimes.com/services/xml/rss/nyt/Business.xml'))

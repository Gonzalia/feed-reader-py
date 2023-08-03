from src.feed.article import Article
from src.feed.feed import Feed
import xml.etree.ElementTree as ET
from src.helpers.constants import Constants


class RssParser:

    def parse_for_rss(response_xml: str):

        f = Feed(Constants.PARSER)

        try:
            root = ET.fromstring(response_xml)

            for item in root.findall('.//item'):
                f.add_article(Article(
                    title=item.findtext(Constants.TITLE),
                    text=item.findtext(Constants.DESCRIPTION),
                    link=item.findtext(Constants.LINK),
                    publication_date=item.findtext(Constants.PUBDATE)
                ))
        except Exception as e:
            print(f'An error has occurred parsing the xml: {e}')

        return f.get_article_list()

from src.feed.article import Article
from src.feed.feed import Feed
import xml.etree.ElementTree as ET
from datetime import datetime


class RssParser:

    def parse_for_rss(response_xml: str):

        f = Feed('Parser')
        root = ET.fromstring(response_xml)

        for item in root.findall('.//item'):
            f.add_article(Article(
                title=item.findtext('title'),
                text=item.findtext('description'),
                link=item.findtext('link'),
                publication_date=item.findtext('pubDate')
            ))

        return f.get_article_list()

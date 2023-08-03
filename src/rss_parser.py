from src.feed.article import Article
from src.feed.feed import Feed
import xml.etree.ElementTree as ET
from datetime import datetime



class RssParser:

    def parse_for_rss(response_xml:str):

        f = Feed('Parser')

        tree = ET.parse(response_xml)
        root = tree.getroot()

        for item in root.findall('.//item'):
            f.add_article(Article(
                title=item.find('title').text,
                description = item.find('title').text,
                link=item.find('link').text,
                publication_date=datetime.strptime(item.find('pubdate').text)
            ))

        return f.get_article_list()
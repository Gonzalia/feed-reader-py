from src.feed.feed import Feed
from src.httpRequest.http_requester import HttpRequester
from src.rss_parser import RssParser
from src.subscription_parser import SubscriptionParser


class FeedReaderMain:
    def main():
        list_of_links = SubscriptionParser.subscription_parser()

        feed = Feed('Main')
        for sub_elem in list_of_links.get_subscriptions_list():
            response_xml = HttpRequester.get_feed(sub_elem.get_url())
            feed.set_article_list(RssParser.parse_for_rss(response_xml))
            feed.pretty_print()


if __name__ == "__main__":
    FeedReaderMain.main()

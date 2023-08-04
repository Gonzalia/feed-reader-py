class SingleSubscription:
    def __init__(self, url, url_params, url_type):
        self.url = url
        self.url_params = [] if url_params is None else url_params
        self.url_type = url_type

    def get_url(self):
        return self.url

    def set_url(self, url):
        self.url = url

    def get_url_params(self):
        return self.url_params

    def get_url_param(self, i):
        return self.url_params[i]

    def set_url_param(self, url_param):
        self.url_params.append(url_param)

    def get_url_params_size(self):
        return len(self.url_params)

    def get_url_type(self):
        return self.url_type

    def set_url_type(self, url_type):
        self.url_type = url_type

    def __str__(self):
        return "{{url={}, url_params={}, url_type={}}}".format(self.get_url(), self.get_url_params(), self.get_url_type())

    def pretty_print(self):
        print(self.__str__())

    def get_feed_to_request(self, i):
        return self.get_url().replace("%s", self.get_url_param(i))


if __name__ == "__main__":
    print("SingleSubscriptionClass")
    s = SingleSubscription(
        "https://rss.nytimes.com/services/xml/rss/nyt/%s.xml", None, "rss")
    s.set_url_param("Business")
    s.set_url_param("Technology")
    print(f"\n{s.get_feed_to_request(0)}")
    s.pretty_print()

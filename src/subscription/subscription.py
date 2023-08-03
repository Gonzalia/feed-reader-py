from subscription.single_subscription import SingleSubscription

class Subscription:
    def __init__(self, subscription_file_path):
        self.subscription_file_path = subscription_file_path
        self.subscriptionsList = []

    def get_subscriptions_list(self):
        return self.subscriptionsList

    def add_single_subscription(self, s):
        self.subscriptionsList.append(s)

    def get_single_subscription(self, i):
        return self.subscriptionsList[i]


    def __str__(self):
        str_ = ""
        for s in self.get_subscriptions_list():
            str_ += s.__str__()
        return "[" + str_ + "]"

    def pretty_print(self):
        print(self.__str__())


if __name__ == "__main__":
    a = Subscription(None)

    s0 = SingleSubscription("https://www.chicagotribune.com/arcio/rss/category/%s/?query=display_date:[now-2d+TO+now]&sort=display_date:desc", [], "rss")
    s0.set_ulr_param("business")

    s1 = SingleSubscription("https://rss.nytimes.com/services/xml/rss/nyt/%s.xml", [], "rss")
    s1.set_ulr_param("Business")
    s1.set_ulr_param("Technology")

    a.add_single_subscription(s0)
    a.add_single_subscription(s1)
    a.pretty_print()
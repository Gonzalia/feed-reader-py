from datetime import datetime
from article import Article

class Feed:
    def __init__(self, site_name):
        self.site_name = site_name
        self.article_list = []

    def get_site_name(self):
        return self.site_name

    def set_site_name(self, site_name):
        self.site_name = site_name

    def get_article_list(self):
        return self.article_list

    def set_article_list(self, article_list):
        self.article_list = article_list

    def add_article(self, article):
        self.article_list.append(article)

    def get_article(self, i):
        return self.article_list[i]

    def get_number_of_articles(self):
        return len(self.article_list)

    def pretty_print(self):
        for article in self.article_list:
            article.pretty_print()

if __name__ == "__main__":
    a1 = Article("This Historically Black University Created Its Own Tech Intern Pipeline",
                 "A new program at Bowie State connects computing students directly with companies, bypassing an often harsh Silicon Valley vetting process",
                 datetime.now(),
                 "https://www.nytimes.com/2023/04/05/technology/bowie-hbcu-tech-intern-pipeline.html"
                )

    a2 = Article("This Historically Black University Created Its Own Tech Intern Pipeline",
                 "A new program at Bowie State connects computing students directly with companies, bypassing an often harsh Silicon Valley vetting process",
                 datetime.now(),
                 "https://www.nytimes.com/2023/04/05/technology/bowie-hbcu-tech-intern-pipeline.html"
                )

    a3 = Article("This Historically Black University Created Its Own Tech Intern Pipeline",
                 "A new program at Bowie State connects computing students directly with companies, bypassing an often harsh Silicon Valley vetting process",
                 datetime.now(),
                 "https://www.nytimes.com/2023/04/05/technology/bowie-hbcu-tech-intern-pipeline.html"
                )

    f = Feed("nytimes")
    f.add_article(a1)
    f.add_article(a2)
    f.add_article(a3)

    f.pretty_print()

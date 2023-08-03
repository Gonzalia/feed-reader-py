from datetime import datetime

class Article:
    
    def __init__(self, title, text, publication_date, link):
        self.title = title
        self.text = text
        self.publication_date = publication_date
        self.link = link
        self.named_entity_list = []

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text

    def get_publication_date(self):
        return self.publication_date

    def set_publication_date(self, publication_date):
        self.publication_date = publication_date

    def get_link(self):
        return self.link

    def set_link(self, link):
        self.link = link

    def add_named_entity(self, named_entity):
        self.named_entity_list.append(named_entity)

    def __str__(self):
        return "Article [title={}, text={}, publication_date={}, link={}]".format(
            self.title, self.text, self.publication_date, self.link
        )
    
    def pretty_print(self):
        print("**********************************************************************************************")
        print("Title: ", self.get_title())
        print("Publication Date: ", self.get_publication_date())
        print("Link: ", self.get_link())
        print("Text: ", self.get_text())
        print("**********************************************************************************************")



# Ejemplo de uso:
if __name__ == "__main__":
    # Crear una instancia de Article
    article = Article(
        title="Título del artículo",
        text="Texto del artículo",
        publication_date=datetime(2023, 8, 2),
        link="https://www.example.com/article"
    )

    # Llamar al método pretty_print para imprimir los detalles del artículo de forma legible
    article.pretty_print()
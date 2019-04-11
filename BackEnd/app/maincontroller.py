from jndcontrollers import ArticleJndController,DomainJndController,ArticlecategorieJndController,CategorieJndController,GeotagJndController

class MainController(ArticleJndController,DomainJndController,ArticlecategorieJndController,CategorieJndController,GeotagJndController):

    def __init__(self):
        pass
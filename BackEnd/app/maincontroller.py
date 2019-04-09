from jndcontrollers import ArticleJndController,ArticlecategorieJndController,CategorieJndController,GeotagJndController

class MainController(ArticleJndController,ArticlecategorieJndController,CategorieJndController,GeotagJndController):

    def __init__(self):
        pass
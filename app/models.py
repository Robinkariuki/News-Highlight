class Source:

    '''
    source class to define news object
    
    '''

    def __init__(self, id, name,description,url,category):

        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
    
class Article:
    '''
    Article class to define Article Objects
    '''
    all_articles = []

    def __init__(self, author, title, description, urlToImage,  publishedAt, content):
        self.author = author
        self.title = title 
        self.description = description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
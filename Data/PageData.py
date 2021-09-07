from bs4 import BeautifulSoup

class PageData:
    def __init__(self):
        pass

    def get_current_title(self, page):
        bs = BeautifulSoup(page, "html.parser") 
        titles = bs.find_all("div", "title")
        return titles
        # url = titles[0]("a")[0]["href"]
        # print(url)
        # return titles

    def get_title(self, date):
        pass

    def get_date(self, partial_page):
        bs = BeautifulSoup(partial_page, "html.parser") 
        date = bs.find_all("div", "date")
        # for item in date:
        #     print(item)

        # print("check B") 
        return date

    def pageToJSON(self, page):
        bs = BeautifulSoup(page, "html.parser")
        article = bs.find_all("div", "author")
        date = bs.find_all("div", "date")
        title = bs.find_all("div", "title")

        information = dict()

        print(article, date, title)


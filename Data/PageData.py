from bs4 import BeautifulSoup
import json

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

    def pageToJSONArray(self, page):
        bs = BeautifulSoup(page, "html.parser")
        author = bs.find_all("div", {"class": "author"})
        date = bs.find_all("div", {"class": "date"})
        title = bs.find_all("div", {"class": "title"})

        # print(title[0].text)
        result = []
        information = dict()
        for index in range(len(date)):
            information['author'] = author[index].get_text()
            information['date'] = date[index].get_text()
            information['title'] = title[index].get_text().replace("\n", "")
            # information['href'] = title[0]('a')[0]["href"]
            # print(information)
            # print(json.dumps(information, ensure_ascii=False))
            result.append(json.dumps(information, ensure_ascii=False))

        print(result)
        return result


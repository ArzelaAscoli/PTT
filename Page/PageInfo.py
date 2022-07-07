import time
import requests
from bs4 import BeautifulSoup


class PageInfo:

    def __init__(self):
        self.PTT = "https://www.ptt.cc"
        self.URL = "/bbs/Gossiping/index.html"

    def get_page(self, url):
        # ppt_header = {"cookies":"over18=1"}
        ptt_cookies = {"over18": "1"}
        response = requests.get(url, cookies=ptt_cookies)
        if response.status_code !=200:
            print("check A")
            return None
        else:
            return response.text

    def get_prev_page_url(self, page):
        bs = BeautifulSoup(page, "html.parser") 
        btn = bs.find_all('div', "btn-group btn-group-paging")
        # print(btn)
        href = btn[0]("a")[1]["href"]
        # print(href)
        return href

    # def get_today_page(self):
    #     today = time.strftime("%m/%d", time.localtime()).lstrip("0")
    #     print(today)

    #     current_page = self.get_page(self.PTT+self.URL)
    #     date = PageData.PageData().get_date(current_page)
    #     print(date)

    #     for index in range(1):
    #         prev_url = self.get_prev_page_url(current_page)
    #         current_page = self.get_page(self.PTT+prev_url) + current_page
    #         # date = PageData.PageData().get_date(current_page).append(date)
        
    #     return current_page

import time
import requests
from bs4 import BeautifulSoup

class PageInfo:

    def __init__(self, domain):
        self.domain = domain

    def get_current_page(self, url):
        # url = self.PTT + url
        # ppt_header = {"cookies":"over18=1"}
        ptt_cookies = {"over18": "1"}
        response = requests.get(url, cookies=ptt_cookies)
        if response.status_code !=200:
            print("check A")
            return None
        else:
            # print(response.text)
            return response.text

    def get_prev_page(self, url):
        page = self.get_current_page(url)
        bs = BeautifulSoup(page, "html.parser") 
        btn = bs.find_all('div', "btn-group btn-group-paging")
        # print(btn)
        href = btn[0]("a")[1]["href"]
        # print(href)
        return self.get_current_page(self.domain+url)

    def get_today_page(self):
        pass

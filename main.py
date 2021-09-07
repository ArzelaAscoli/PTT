from urllib import request
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError


PTT = "https://www.ptt.cc"
URL = "/bbs/Gossiping/index.html"

def Initial():
    print("=== Let's go to Gossiping ===")

def get_page(url):
    url = PTT + url
    # ppt_header = {"cookies":"over18=1"}
    ptt_cookies = {"over18": "1"}
    response = requests.get(url, cookies=ptt_cookies)
    if response.status_code !=200:
        print("check A")
        return None
    else:
        # print(response.text)
        return response.text

def prev_page_url(page):
    bs = BeautifulSoup(page, "html.parser") 
    btn = bs.find_all('div', "btn-group btn-group-paging")
    # print(btn)
    href = btn[0]("a")[1]["href"]
    # print(href)
    return href

def get_title(page):
    bs = BeautifulSoup(page, "html.parser") 
    titles = bs.find_all("div", "title")
    url = titles[0]("a")[0]["href"]
    print(url)
    return titles

if __name__ == '__main__':

    Initial()
    page = get_page(URL)
    current_title = get_title(page)



    # prev_url = prev_page_url(page)
    # page = get_page(prev_url)
    # prev_title = get_title(page)
    # print(prev_title, current_title)


import json
import time
from Page import PageInfo
from Data import PageData


PTT = "https://www.ptt.cc"
URL = "/bbs/Gossiping/index.html"


def remove_button(data):
    for item in data:
        title = json.loads(item)["title"]
        if "八卦板板規" in title:
            data = data[:data.index(item)]
            break
    return data

def get_today_article():
    getPage = PageInfo.PageInfo()
    getData = PageData.PageData()
    today = time.strftime("%m/%d", time.localtime()).lstrip("0")

    current_page = getPage.get_page(PTT+URL) # get current page
    page_data = getData.pageToJSONArray(current_page)
    page_data = remove_button(page_data)

    for item in page_data:
        if json.loads(item)["date"] != today:
            page_data = page_data[page_data.index(item):]

    count = 1
    flag = True
    while flag: # previous page
        prev_url = getPage.get_prev_page_url(current_page)
        current_page = getPage.get_page(PTT+prev_url)
        page_data_temp = getData.pageToJSONArray(current_page)

        if json.loads(page_data_temp[0])["date"] != today:
            for item in page_data_temp:
                if json.loads(item)["date"] == today:
                    page_data_temp = page_data_temp[page_data_temp.index(item):]
                    page_data = page_data_temp + page_data
                    flag = False
                    break
        else:
            page_data = page_data_temp + page_data

        count = count +1
        print("check")
        
    print(count)
    return page_data


if __name__ == '__main__':

    print("=== Let's go to Gossiping ===")
    getPage = PageInfo.PageInfo()
    getData = PageData.PageData()

    page = getPage.get_page(PTT+URL)    
    prev_url = getPage.get_prev_page_url(page)
    page = getPage.get_page(PTT+prev_url) 
    page_data = getData.pageToJSONArray(page)

    today = get_today_article()
    print(today)




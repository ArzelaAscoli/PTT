from Page import PageInfo
from Data import PageData

PTT = "https://www.ptt.cc"
URL = "/bbs/Gossiping/index.html"


if __name__ == '__main__':

    print("=== Let's go to Gossiping ===")
    getPage = PageInfo.PageInfo(PTT)
    getData = PageData.PageData()

    page = getPage.get_current_page(PTT+URL)
    title = getData.get_current_title(page)
    date = getData.get_date(page)
    getData.pageToJSON(page)


    # print(page)
    # title = getData.get_title(page, )


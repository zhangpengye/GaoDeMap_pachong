import requests
import codecs
import time
from bs4 import BeautifulSoup
# 网页的请求头
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
}

def get_page(url):
    response = requests.get(url, headers=header)

    # 通过BeautifulSoup进行解析出每个房源详细列表并进行打印
    soup_idex = BeautifulSoup(response.text, 'html.parser')
    result_li = soup_idex.find_all('li', {'class': 'list-item'})

    # 进行循环遍历其中的房源详细列表
    for i in result_li:
        # 由于BeautifulSoup传入的必须为字符串，所以进行转换
        page_url = str(i)
        soup = BeautifulSoup(page_url, 'html.parser')
        # 由于通过class解析的为一个列表，所以只需要第一个参数
        result_href = soup.find_all('a', {'class': 'houseListTitle'})[0]
        # 详细页面的函数调用
        get_page_detail(result_href.attrs['href'])


    # 进行下一页的爬取
    result_next_page = soup_idex.find_all('a', {'class': 'aNxt'})
    if len(result_next_page) != 0:
        # 函数进行递归
        get_page(result_next_page[0].attrs['href'])
        time.sleep(1)
    else:
        print('没有下一页了')

# 进行字符串中空格，换行，tab键的替换及删除字符串两边的空格删除
def my_strip(s):
    return str(s).replace(" ", "").replace("\n", "").replace("\t", "").strip()
# 由于频繁进行BeautifulSoup的使用，封装一下，很鸡肋
def my_Beautifulsoup(response):
    return BeautifulSoup(str(response), 'html.parser')



# 详细页面的爬取
def get_page_detail(url):
    response = requests.get(url, headers=header)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # 标题什么的一大堆，哈哈
        result_title = soup.find_all('h3', {'class': 'long-title'})[0]
        result_price = soup.find_all('span', {'class': 'light info-tag'})[0]
        f.write(str(result_title))
        f.write(str(result_price))
if __name__ == '__main__':
    # url链接
    f = codecs.open('D:/Python34/b.txt','w','utf-8')
    url = 'https://zibo.anjuke.com/sale/m731'
    # 页面爬取函数调用
    get_page(url)
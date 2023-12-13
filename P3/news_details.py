from bs4 import BeautifulSoup
from click_counts import *


def data_refine(html_content, url):    # 使用BeautifulSoup对htm内容进行解析，从而获取到对应的数据
    soup = BeautifulSoup(html_content, 'html.parser')
    title = soup.find('div', class_='detail-title').text
    date = soup.find('div', class_='detail-infor').find_all('span')[1].text.strip().split('：')[1]

    click_count = link_combine(link_split(url))  # 点击量使用了单独的函数进行获取

    content = soup.find('div', class_='v_news_content').text.strip()
    name = soup.find('div', class_='bread').find_all('a')[1].text
    source = soup.find('div', class_='detail-infor').find_all('span')[0].text.split('：')[1]

    return title, date, click_count, content, name, source



from bs4 import BeautifulSoup
from request_htm import *


def side_link(url):
    html_content = replace_absolute(request_htm(url))
    soup = BeautifulSoup(html_content, 'html.parser')
    htm_path = soup.find('div', class_='bd').find_all('a')

    list_link = []
    for i in range(0, len(htm_path)):
        htm_path = soup.find('div', class_='bd').find_all('a')[i].attrs['href']
        list_link.append(htm_path)
    return list_link  # 返回带侧边栏链接的list


if __name__ == '__main__':
    print(side_link('https://www.yibinu.edu.cn/xwzx/xxyw.htm'))

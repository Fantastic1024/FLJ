from news_allpages import *
from news_details import *


def page_link(url):
    html_content = replace_absolute(request_htm(url))
    soup = BeautifulSoup(html_content, 'html.parser')
    htm_path = soup.find_all('div', class_='title')

    list_temp = []

    for n in range(0, len(htm_path)):
        htm_path = soup.find_all('div', class_='title')[n].find('a').attrs['href']
        list_temp.append(htm_path)

    return list_temp  # 此处返回每页的所有新闻链接


def all_link():  # 将所有新闻的链接保存至一个txt文档中
    side_lists = side_link('https://www.yibinu.edu.cn/xwzx/xxyw.htm')  # 得到侧边栏的6个链接并保存至side_lists中

    with open('all_info_pages.txt', 'w') as file:
        for n in range(0, 6):  # 侧边栏的6个页面，获取其中每一个页面的所有链接
            for m in range(0, len(home_page(side_lists[n]))):
                list_data = page_link(home_page(side_lists[n])[m])
                file.write(str(list_data) + '\n')
                print('Writing to all_info_pages.txt')

    print("已成功获取到所有新闻的链接并保存到all_info_pages.txt")

    # return all_link_list


if __name__ == '__main__':
    all_link()  # 爬取到的所有新闻链接

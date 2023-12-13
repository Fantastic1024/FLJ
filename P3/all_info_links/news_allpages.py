from news_sidebars import *

# 一个页面的所有链接
sides_list = side_link('https://www.yibinu.edu.cn/xwzx/xxyw.htm')


def home_page(url):  # 将网址插入页码
    html_content = replace_absolute(request_htm(url))
    soup = BeautifulSoup(html_content, 'html.parser')
    htm_path = soup.find('span', class_='p_no').find('a').attrs['href']
    # print(htm_path)

    page_num2 = int(re.search(r'\d+', htm_path).group())  # 获取不同页面的第二页的页数，使用正则

    # print(page_num2)
    list_link_2 = [url]
    for p_num in range(page_num2, 0, -1):  # 倒序生成数字
        number_to_insert = p_num  # 你要插入的数字

        # 替换 .htm 为  /+数字+.htm
        new_url = re.sub(r'\.htm', f'/{number_to_insert}.htm', url)

        list_link_2.append(new_url)
    return list_link_2  # 返回插入页面之后带页码的所有link的list


if __name__ == '__main__':
    for i in range(0, 6):
        print(home_page(sides_list[i]))

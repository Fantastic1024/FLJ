from request_htm import *
import re


def link_combine(usernewsids):
    # usernewsids = '56471'
    owner = '1397404744'
    clicktype = 'wbnews'
    click_url = f'https://www.yibinu.edu.cn/system/resource/code/news/click/dynclicksbatch.jsp?clickids={usernewsids}&owner={owner}&clicktype={clicktype}'

    count = request_htm(click_url)  # 使用get从数据库获取到不同新闻页面的点击量

    return count


def link_split(url):
    # 使用正则表达式获取了.htm前部分的数字作为usernewsids
    pattern = r'(\d+)(?=\.htm)|(?<=\.htm)(\d+)'

    # Using regular expression to find the numbers
    matches = re.findall(pattern, url)
    return matches[0][0]
    # 返回usernewsids


if __name__ == '__main__':
    url = 'https://www.yibinu.edu.cn/info/1049/56471.htm'
    print(link_split(url))
    print(link_combine(link_split(url)))

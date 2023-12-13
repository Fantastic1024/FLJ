import re
from urllib.parse import urljoin
import requests


def request_htm(url):  # 获取htm页面并返回htm_content网页源码
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/54.0.2840.99 Safari/537.36"}
    response = requests.get(f'{url}', headers=headers)
    response.encoding = "utf-8"
    html_content = response.text
    return html_content


def replace_absolute(html_content):  # 用正则表达式将获取到的htm_content中的相对路径全部转换为绝对路径
    base_url = 'https://www.yibinu.edu.cn/xwzx/'

    html_content = re.sub(r'href="([^"]+)"', lambda m: f'href="{urljoin(base_url, m.group(1))}"', html_content)

    return html_content


if __name__ == '__main__':
    modified_html_content = replace_absolute(request_htm('https://www.yibinu.edu.cn/info/1048/21472.htm'))
    print(modified_html_content)
    # print(request_htm())

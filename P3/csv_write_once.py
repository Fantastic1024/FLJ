import ast
import threading
import csv
from news_details import *
from request_htm import *


def write_to_csv(link, lock, semaphore):  # 使用多线程将每一页爬取到的数据保存至csv，同时使用线程锁保证每次只有一个线程写入csv
    with semaphore:
        html_content = replace_absolute(request_htm(link))
        title, date, click_count, content, name, source = data_refine(html_content, link)
        with lock:
            with open('output.csv', 'a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([title, date, click_count, content, name, source, link])
                print(f"Thread {threading.current_thread().name} wrote data for {title}")


# 初始化 Semaphore，设定最大线程数，例如 10
max_threads = 50
semaphore = threading.Semaphore(max_threads)

# 创建一个锁对象
lock = threading.Lock()

# 创建多个线程来处理 HTML 内容并写入数据
threads = []

with open('all_info_pages.txt', 'r', encoding='utf-8') as file:
    file_content = file.readlines()

links = []
for line in file_content:
    # 将字符串表示的列表转换为真正的列表
    links.extend(ast.literal_eval(line.strip()))

for link in links:
    thread = threading.Thread(target=write_to_csv, args=(link, lock, semaphore))
    threads.append(thread)
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()

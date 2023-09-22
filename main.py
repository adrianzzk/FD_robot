import requests  
from lxml import etree  
import concurrent.futures  
from pyfiglet import Figlet  
import time  
import traceback  
import datetime  
import urllib  
from config import *




def check_updates(url_alias):

    """
    检查指定URL是否有更新的文档
    :param url_alias: URL的别名及相关配置信息字典
    :return: (是否有更新, 更新的文档列表)
    """

    url = url_alias['url']
    response = requests.get(url).content                                # 获取URL的内容
    doc = etree.HTML(response)                                          # 使用lxml库解析HTML文档

    publish_dates = doc.xpath(url_alias['publish_date_xpath'])          # 提取发布日期
    doc_urls = doc.xpath(url_alias['doc_url_xpath'])                    # 提取文档URL
    doc_titles = doc.xpath(url_alias['doc_title_xpath'])                # 提取文档标题

    updated = False                                                     # 是否有更新的标志
    updated_docs = []                                                   # 更新的文档列表

    max_time = max(publish_dates, default='0')                          # 获取发布日期最大值
    max_time_num = max_time.replace("-", "")                            # 转换为数字格式
    if max_time_num <= TARGET_DATE:                                     # 如果最大日期小于等于目标日期，则无更新
        return updated, updated_docs

    for i, date in enumerate(publish_dates):
        date_num = date.replace("-", "")                                # 转换为数字格式

        if date_num > TARGET_DATE:                                      # 如果日期大于目标日期，则有更新
            updated = True
            doc_url = doc_urls[i]
            if not doc_url.startswith('https://'):
                doc_url = urllib.parse.urljoin(url, doc_url)            # 处理相对URL,变成可访问的绝对URL
            updated_docs.append((doc_titles[i], doc_url))               # 添加更新的文档信息到列表

    return updated, updated_docs



def process_url(url_key):

    """
    处理URL，检查是否有更新并打印更新信息
    :param url_key: URL的别名及相关配置信息字典
    :return: 是否有更新
    """

    alias = url_key['alias']
    updated, updated_docs = check_updates(url_key)                      # 检查更新

    if updated:
        update_count = len(updated_docs)                                # 更新的文档数量
        print(f"{alias} has updates:\n")

        for title, link in updated_docs:
            print(f"{title}: {link}\n")                                 # 打印更新的文档信息

        print(f"Total {alias} updates: {update_count}\n")               # 打印总更新数

    return updated



def print_large_text(text):

    """
    打印大号文本艺术字
    :param text: 待打印的文本
    """

    f = Figlet(font='big')
    ascii_text = f.renderText(text)
    #ascii_text = f"\033[31m{ascii_text}\033[0m"                        # 使用红色显示
    print(ascii_text)



def main():

    """
    主函数，控制程序的执行流程
    """

    run = True

    if len(TARGET_DATE) != 8:
        run = False
        print('wrong target date you put')

    if len(MONITORED_URLS) == 0:
        run = False
        print('no monitored urls')

    while run:
        current_time = datetime.datetime.now().strftime("%Y.%m.%d %H:%M")               # 获取当前时间
        print(f"{current_time} update:")

        with concurrent.futures.ThreadPoolExecutor() as executor:                       # 创建线程池
            results = executor.map(process_url, 
                                   [URL_ALIAS[url] for url in MONITORED_URLS])          # 并发处理URL

        has_updates = any(results)                                                      # 检查是否有更新

        if not has_updates:
            print_large_text(NO_UPDATE_TEXT)                                            # 打印未更新文本

        try:
            time.sleep(SLEEP_TIME)                                                      # 休眠一段时间
        except KeyboardInterrupt:
            print("Program interrupted by user")                                        # 用户中断程序
            break
        except Exception as e:
            print(f"Error occurred: {traceback.format_exc()}")                          # 打印异常信息
            continue




if __name__ == '__main__':
    main()  
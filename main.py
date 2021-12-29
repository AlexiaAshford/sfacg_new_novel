# coding:utf-8
import requests
import re
import datetime

preorder_url_list = []
days_number = 0

for i in range(100):
    days_number += 7
    result = datetime.datetime(2022, 1, 1) + datetime.timedelta(days=-days_number)
    time_ = result.strftime("%Y-%m-%d").replace('-', '')
    preorder_url_list.append(
        [result.strftime("%Y-%m-%d"), f'https://pages.sfacg.com/ajax/act/PreOrder.ashx?op=getPreOrderNovels&date={time_}']
    )

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, '
                  'like Gecko) Version/5.1 Safari/534.50 '
}


def dealData(time_data, url):
    result_ = requests.get(url, headers=headers).json()
    print(url)
    if result_.get('status') == 200:
        result_data = result_.get('data')
        for data in result_data:
            novel_name = data.get('novelName')
            book_id = data.get('novelId')
            cover = data.get('cover')
            is_main_push = data.get('isMainPush')
            tags = ','.join(data.get('tags'))
            intro = re.sub('<br/>', '\n', data.get('intro'))

            show_info = '书名:{}\n序号:{}\n封面:{}\n是否上推:{}\n标签:{}\n简介:{}\n'
            show_info = show_info.format(
                novel_name, book_id, cover, is_main_push, tags, intro
            )
            print(show_info)
            open(str(time_data), 'w', encoding='utf-8').write(show_info)

for url in preorder_url_list:
    dealData(url[0], url[1])

import requests
from rich import print
import re


def str_mid(string: str, left: str, right: str, start=None, end=None):
    pos1 = string.find(left, start, end)
    if pos1 > -1:
        pos2 = string.find(right, pos1 + len(left), end)
        if pos2 > -1:
            return string[pos1 + len(left): pos2]
    return ''


headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/96.0.4664.110 Mobile Safari/537.36 Edg/96.0.1054.62 '
}


def get(url, **kwargs):
    params = kwargs.get("params")
    try:
        return requests.get(url, params=params, headers=headers).text
    except Exception as e:
        print("get请求错误: %s" % e)


chapterurl_list = []
result = get('https://book.sfacg.com/Novel/492364/MainIndex/')
# print(result)
dir_ = str_mid(result, '<ul class="mulu_list">', '<div class="bottom_menu">')
html_list = dir_.replace('\r\n<a href="/c/', '/"><li>').split('/"><li>')
for chapterid in html_list:
    if chapterid.isdigit():
        chapterurl_list.append('https://book.sfacg.com/Novel/492364/659995/{}'.format(chapterid))
# print(chapterurl_list)

for url in chapterurl_list:
    chapter_result = get(url)
    title = str_mid(chapter_result, '返回</a></li><li>', '</li>')
    content = str_mid(chapter_result, '<div style="text-indent: 2em;">', '</p></div>')
    content = re.sub('</p>', '\n', content)
    content = re.sub('<p>', '　　', content)
    print(title)
    print(content)
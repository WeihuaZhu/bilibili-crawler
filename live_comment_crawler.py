# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}

def bv2av(url):
    """
    convert a bilibili video url with newest encoding bv to its original av number
    :param url: bilibili video url <str>
    :return: av_id <int>
    """
    r = requests.get(url, headers=HEADERS)
    try:
        av = re.findall(r"video/av(\d+)/", r.text)[0]
        return av
    except Exception as e:
        print(e)
        raise

def main():

    av_id = bv2av('https://www.bilibili.com/video/BV1cC4y1a7xA')

    resp = requests.get('https://www.bilibili.com/video/av' + av_id, headers=HEADERS)
    match_rule = r'cid=(.*?)&aid'
    oid = re.search(match_rule, resp.text).group().replace('cid=', '').replace('&aid', '')
    print('oid=' + oid)

    # xml_url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=' + oid
    xml_url = 'https://comment.bilibili.com/{}.xml'.format(oid)
    resp = requests.get(xml_url, headers=HEADERS)
    content = resp.content
    content_text = content.decode('utf-8')
    xml_soup = BeautifulSoup(content_text, 'xml')
    all_ds = xml_soup.find_all('d')
    all_live_comments = [item.text for item in all_ds]
    print(all_live_comments)

if __name__ == "__main__":
    main()
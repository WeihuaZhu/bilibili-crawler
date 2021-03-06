# -*- coding: utf-8 -*-
import re
import requests
from bs4 import BeautifulSoup
import jieba.posseg as pseg
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np

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

def parse_words(all_texts):
    # res = pseg.cut("我爱北京天安门")
    # for word, flag in res:
    #     print(str(word))
    words = []
    for entry in all_texts:
        parse_result = pseg.cut(entry)
        for word, _ in parse_result:
            words.append(str(word))
    return words

def generate_word_cloud(words):
    text = "/".join(words)
    print(text)
    wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white", font_path='fonts/MSYH.TTC').generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

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
    parsed_words = parse_words(all_live_comments)
    generate_word_cloud(parsed_words)

if __name__ == "__main__":
    main()
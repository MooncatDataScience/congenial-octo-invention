# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 18:02:43 2022

@author: Takodachi
"""

import requests
import jieba
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup

# get web
response = requests.get("")

#soup解析
soup = BeautifulSoup(response.text, "html.parser")

#搜尋符合的節點
result = soup.find_all("")

#加入array
text = []
for r in result:
    text.append(r.select_one("a").getText())
    
#製作文本
words = ""
for t in text:
    words += str(t)
    
#斷詞 中文:Jieba 英文:NLTK
jieba.load_userdict('./userdict.txt')#客製化斷詞

#讀取和使用停用詞彙
def get_stopword_list(file):
    with open(file, encoding='utf-8')as f:
        stopword_list = [word.strip('\n') for word in f.readlines()]
    return stopword_list

def get_jieba_table(lst,v=None):
    jieba.set_dictionary("dict.txt")
    stop = get_stopword_list("stop2.txt")
    jie = list(jieba.cut(lst))
    list_difference = [element for element in jie if element not in stop]
    return list_difference


clean_table = get_jieba_table(words)
string = " ".join(clean_table)

#製作文本

    

#生成文字雲
import wordcloud
wc = wordcloud.WordCloud(background_color="white", repeat=True).generate(string)

#繪圖
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 06:03:19 2022

@author: Takodachi
"""

import requests
import jieba
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup


#取得Link
response = requests.get("https://www.thenewslens.com/category/world")

#soup解析
soup = BeautifulSoup(response.text, "html.parser")

#print html content
#print(soup.prettify)

#搜尋符合的節點
result = soup.find_all("h2")
#print(result)

#去除tag標籤 print確認
# for r in result:
#     print(r.select_one("a").getText()) 
    #select_one 尋找h2底下有a標籤getText()取得
    
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
# cut = jieba.lcut(word, cut_all=False)
# dictionary = Counter(cut)


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

#生成文字雲
import wordcloud
wc = wordcloud.WordCloud(background_color="white", repeat=True).generate(string)

#繪圖
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

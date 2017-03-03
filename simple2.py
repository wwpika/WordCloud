#-*- coding:utf-8 -*-
from os import path
from wordcloud import WordCloud

d=path.dirname(__file__)

font=path.join(path.dirname(__file__),"simsun.ttc")
text=open(u'santi.txt').read().decode('utf-8')

wordcloud=WordCloud(font_path=font).generate(text)

import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")


wordcloud=WordCloud(font_path=font,max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
plt.show()
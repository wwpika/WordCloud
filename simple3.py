#-*- coding:utf-8 -*-
import numpy as np 
from PIL import Image
from os import path
import matplotlib.pyplot as plt 
import random
import os

from wordcloud import WordCloud,STOPWORDS

font=path.join(path.dirname(__file__),"simsun.ttc")

def grey_color_func(word,font_size,position,orientation,random_state=None,**kwargs):
	return "hsl(0,0%%,%d%%)" % random.randint(60,100)

d=path.dirname(__file__)

#numpy.array:生成一个数组
mask=np.array(Image.open(path.join(d,"ka.png")))

text=open(u"santi.txt").read().decode('utf-8')

text=text.replace(u"程心说",u"程心")
text=text.replace(u"程心和",u"程心")
text=text.replace(u"程心问",u"程心")

stopwords=set(STOPWORDS)
stopwords.add("int")
stopwords.add("ext")

wc=WordCloud(font_path=font,max_words=2000,mask=mask,stopwords=stopwords,margin=10,
				random_state=1).generate(text)

default_colors=wc.to_array()
plt.title("Custom colors")
#Display an image on the axes 
plt.imshow(wc.recolor(color_func=grey_color_func,random_state=3))
wc.to_file("a_new_hope.png")
plt.axis("off")
#Creates a new figure
plt.figure()
plt.title(u"SanTi-TongJi")
plt.imshow(default_colors)
#Convenience method to get or set axis properties
plt.axis("off")
#Display a figure
plt.show() 
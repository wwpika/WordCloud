#-*- coding:utf-8 -*-
from os import path
from wordcloud import WordCloud

#脚本所在路径
d=path.dirname(__file__)

#Read the whole text.
text=open(path.join(d,'constitution.txt')).read()

#Generate a word cloud image
wordcloud=WordCloud().generate(text)

#Display the generated image:
#the matplotlib way:
import matplotlib.pyplot as plt
#Display an image on the axes 
plt.imshow(wordcloud)
#Convenience method to get or set axis properties
plt.axis("off")

#lower max_font_size
wordcloud=WordCloud(max_font_size=40).generate(text)
#Creates a new figure
plt.figure()
plt.imshow(wordcloud)
plt.axis("off")
#Display a figure
plt.show() 
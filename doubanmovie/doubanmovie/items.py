# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy import Item, Field



class DoubanmovieItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #电影名字
    movie_name = Field()
    #电影导演
    movie_director = Field()
    #电影编剧
    movie_writer = Field()
    #电影演员
    movie_roles = Field()
    #电影语言
    movie_language = Field()
    #电影上映时间
    movie_date = Field()
    #电影时长
    movie_long = Field()
    #电影描述
    movie_descripiton = Field()

# -*- coding: utf-8 -*-
import re
import csv
from movie_review.spiders.sql import Mysql_Control
import time
import scrapy
from scrapy.http import Request

Data_year = [
    ['2016_id', '2016_text'],
    ['2017_id', '2017_text'],
    ['2018_id', '2018_text'],
    ['2019_id', '2019_text'],
    ['2020_id', '2020_text']
]

Data_fenlei = [
    ['lishi_id',  'lishi_text'],
    ['kehuan_id', 'kehuan_text'],
    ['wuxia_id',  'wuxia_text'],
    ['xiju_id',   'xiju_text'],
    ['xuanyi_id', 'xuanyi_text']
]


Data_daoyan = [
    ['chenkaige_id',    'chenkaige_text'],
    ['fengxiaogang_id', 'fengxiaogang_text'],
    ['zhangyimou_id',   'zhangyimou_text'],
    ['zhouxingchi_id',  'zhouxingchi_text'],
    ['xuke_id',         'xuke_text']
]



class YingpingSpider(scrapy.Spider):
    name = 'yingping'

    def __init__(self):
        self.mysqls = Mysql_Control()

    def start_requests(self):
        i = 0
        for info in Data_fenlei :
            ret = self.mysqls.select_db(info[0])
            toplist = []
            for id in ret:
                toplist.append(id[0])
            print(info[1])
            for movie_id in toplist:
                print(i)
                i = i+1
                if i < 253:
                    continue
                for start in range(0, 200, 20):
                    meta = {
                        'table_name': info[1]
                    }
                    movie_id = movie_id.replace('\n', '')
                    url = 'https://movie.douban.com/subject/{}/comments?start={}&limit=20&sort=new_score&status=P'.format(movie_id, start)
                    yield Request(url=url, meta=meta)

    def parse(self, response):
        self.mysqls.create_db(response.meta['table_name'])
        review_list = response.xpath('//span[@class="short"]/text()').extract()
        # print(review_list)
        for review in review_list:
            review = review.strip()
            review = review.replace('\t', '')
            review = review.replace('\n', '')
            review = review.replace('\xa0', '')
            review = review.replace('\ufeff', '')
            review = review.replace('\u200b', '')

            if review:
                self.mysqls.insert_db(response.meta['table_name'], review)

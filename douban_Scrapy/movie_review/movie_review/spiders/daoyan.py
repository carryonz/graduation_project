# -*- coding: utf-8 -*-
import re
from movie_review.spiders.sql import Mysql_Control
import time
import scrapy
from scrapy.http import Request

Data = [
    [
        'chenkaige_id',
        [
            'https://movie.douban.com/celebrity/1023040/movies?start=0&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1023040/movies?start=10&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1023040/movies?start=20&format=pic&sortby=vote&role=D'
        ]
    ],
    [
        'zhangyimou_id',
        [
            'https://movie.douban.com/celebrity/1054398/movies?start=0&format=pic&sortby=time&role=D',
            'https://movie.douban.com/celebrity/1054398/movies?start=10&format=pic&sortby=time&role=D',
            'https://movie.douban.com/celebrity/1054398/movies?start=20&format=pic&sortby=time&role=D',
            'https://movie.douban.com/celebrity/1054398/movies?start=30&format=pic&sortby=time&role=D'
        ]
    ],
    [
        'zhouxingchi_id',
        [
            'https://movie.douban.com/celebrity/1048026/movies?start=0&format=pic&sortby=time&role=D',
            'https://movie.douban.com/celebrity/1048026/movies?start=10&format=pic&sortby=time&role=D'
        ]
    ],
    [
        'xuke_id',
        [
            'https://movie.douban.com/celebrity/1007152/movies?start=0&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1007152/movies?start=10&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1007152/movies?start=20&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1007152/movies?start=30&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1007152/movies?start=40&format=pic&sortby=vote&role=D'
        ]
    ],
    [
        'fengxiaogang_id',
        [
            'https://movie.douban.com/celebrity/1274255/movies?start=0&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1274255/movies?start=10&format=pic&sortby=vote&role=D',
            'https://movie.douban.com/celebrity/1274255/movies?start=20&format=pic&sortby=vote&role=D'
        ]
    ]
]

class DaoyanSpider(scrapy.Spider):
    name = 'daoyan'
    
    def start_requests(self):
        for info in Data:
            meta = {
                    'table_name': info[0]
                }
            print (info[0])
            for url in info[1]:
                yield Request(url=url, meta=meta)
                time.sleep(3)

    def parse(self, response):
        mysqls = Mysql_Control()
        mysqls.create_db(response.meta['table_name'])
        movie_urls = response.xpath('//*[@id="content"]/div/div[1]/div[2]/ul/li/dl/dt/a/@href').extract()
        for movie_url in movie_urls:
            p = re.compile(r'\d+')
            movie_id = p.findall(movie_url)[0]
            mysqls.insert_db(response.meta['table_name'], movie_id)
            # with open('./data/daoyan.txt', 'a+') as f:
            #     f.write(movie_id)
            #     f.write('\n')

            # print(movie_id)

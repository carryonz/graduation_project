# -*- coding: utf-8 -*-
import re
import json
import pandas as pd
import scrapy
from scrapy.http import Request
from movie_review.spiders.sql import Mysql_Control
import time

Datas_type = [
    [
        'xiju_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&genres=%E5%96%9C%E5%89%A7',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&genres=%E5%96%9C%E5%89%A7',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&genres=%E5%96%9C%E5%89%A7']
    ],
    [   'kehuan_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&genres=%E7%A7%91%E5%B9%BB',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&genres=%E7%A7%91%E5%B9%BB',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&genres=%E7%A7%91%E5%B9%BB']
    ],
    [
        'xuanyi_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&genres=%E6%82%AC%E7%96%91',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&genres=%E6%82%AC%E7%96%91',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&genres=%E6%82%AC%E7%96%91']
    ],
    [
        'wuxia_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&genres=%E6%AD%A6%E4%BE%A0',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&genres=%E6%AD%A6%E4%BE%A0',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&genres=%E6%AD%A6%E4%BE%A0']
    ],
    [
        'lishi_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&genres=%E5%8E%86%E5%8F%B2',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&genres=%E5%8E%86%E5%8F%B2',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&genres=%E5%8E%86%E5%8F%B2']
    ]
]

Datas_year = [
    [
        '2016_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&year_range=2016,2016',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&year_range=2016,2016',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&year_range=2016,2016']
    ],
    [
        '2017_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&year_range=2017,2017',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&year_range=2017,2017',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&year_range=2017,2017']
    ],
    [
        '2018_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&year_range=2018,2018',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&year_range=2018,2018',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&year_range=2018,2018']
    ],
    [
        '2019_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&year_range=2019,2019',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&year_range=2019,2019',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&year_range=2019,2019']
    ],
    [
        '2020_id',
        ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=0&year_range=2020,2020',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=20&year_range=2020,2020',
        'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=%E7%94%B5%E5%BD%B1&start=40&year_range=2020,2020']
    ]
]

class TypesSpider(scrapy.Spider):
    name = 'types'

    def start_requests(self):
        for info in Datas_year:
            meta = {
                    'table_name': info[0]
                }
            print (info[0])
            for url in info[1]:
                yield Request(url=url, meta=meta)
                time.sleep(3)

    def parse(self, response):
        # print(response.text)
        dicts = json.loads(response.text)
        df = pd.DataFrame(dicts['data'])
        ids = df['id'].str.split('\n')
        mysqls = Mysql_Control()
        print(response.meta['table_name'])
        mysqls.create_db(response.meta['table_name'])
        for movie_id in ids:
            # print (movie_id[0])
            mysqls.insert_db(response.meta['table_name'], movie_id[0])
        
        # ret = mysqls.select_db(response.meta['table_name'])
        # print(type(ret))
        # for id in ret:
        #     print(id[0])
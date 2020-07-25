# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
   url = 'https://movie.douban.com/'
   head = {}
   head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
   req = requests.get(url, headers=head)
   print (req.status_code)
   # soup = BeautifulSoup(res.text,'html.parser')
   # prices_list =soup.findAll('img')

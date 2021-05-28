# -*- coding: utf-8 -*-
"""
Created on Fri May 28 17:21:41 2021

@author: eka susanti
"""

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "Novel"

    def start_requests(self):
        urls = [
	    "https://www.worldnovel.online/novel/another-worlds-versatile-crafting-master/",
	    "https://www.worldnovel.online/novel/scholars-advanced-technological-system/",
	    "https://www.worldnovel.online/novel/super-detective-in-the-fictional-world/", 
        "https://www.worldnovel.online/novel/the-first-order/",
	    "https://www.worldnovel.online/novel/god-of-fishing/",
            ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')
    
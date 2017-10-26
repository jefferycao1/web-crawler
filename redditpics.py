import scrapy

class RedditPicSpider(scrapy.Spider):
	name = "redditpic_spider"
	start_urls = ['http://reddit.com/r/pics']
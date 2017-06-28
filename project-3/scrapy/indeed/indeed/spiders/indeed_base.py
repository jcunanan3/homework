import scrapy
from indeed.items import IndeedItem
from bs4 import BeautifulSoup as bs


class IndeedBaseSpider(scrapy.Spider):
	name = "indeedBase"
	start_urls = ['http://www.indeed.com/q-data-scientist-l-San-Francisco,-CA-jobs.html']

	def parse(self,response):
		#/'//span[@class="company"]/span'
		#//h2/a/@title'
		titles = response.xpath('//h2/a/@title').extract()
		links = response.xpath('//h2/a/@href').extract()
		companies = response.xpath('//span[@class="company"]/span').extract()

		for title,link,company in zip(titles,links,companies):
			item = IndeedItem()
			item['title'] = title
			item['link'] = link
			item['company'] = bs(company).get_text().strip()
			yield item

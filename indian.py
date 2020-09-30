# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from dateutil.parser import parse
import re
import unicodedata

class IndianSpider(scrapy.Spider):
	name = 'indian'
	start_urls = ['https://indianexpress.com/']

	rotate_user_agent = True
	custom_settings = {
						'CONCURRENT_REQUESTS' : 5,
						'DOWNLOAD_DELAY' : 0.5,
						'RETRY_TIMES' : 10,
					}

	def __init__(self,text=None,key=None,*args,**kwargs):
		self.text=text
		self.key=key
	def parse(self,response):
		if ' ' in self.text:
			self.text=self.text.replace(' ','+')
		url="https://indianexpress.com/"+"?s="+str(self.text)
		yield scrapy.Request(url=url,callback=self.parse1)
	def parse1(self,response):
		abc=int(1)
		while abc<3:
			url="https://indianexpress.com/"+"page/"+str(abc)+"/?s="+str(self.text)
			abc+=1
			yield scrapy.Request(url=url,callback=self.parse2)
		
	def parse2(self, response):
		site =response.xpath("//h3/a/@href").extract()
		for sit in site:
			url=sit

			yield scrapy.Request(url=url,callback=self.parse3)

	def parse3(self, response):
		heading = ''.join(response.xpath('//h1/text()').extract()).strip()
		date =''.join(response.xpath("//time[@class='g-header__time']/@datetime").extract())
		if date:
			a=parse(date)
			newdate=datetime.strftime(a,'%d-%m-%Y')
		reviews =''.join(response.xpath('//*[@id="ie_load_native_story"]/div/div/article/div[3]/div/div/p/text()').extract())
		item ={"para":reviews,"date":newdate,"headlines":heading}
		yield item
		

	
				 
	  

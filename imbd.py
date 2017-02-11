from scrapy import Request
from scrapy.spiders import Spider

# from fullpath import path

import collections
#d = collections.OrderedDict()
#scrapy runspider imbd.py -t csv -o imbd.csv

class S1(Spider):
	name = 's1'
	# allowed_domains = "http://www.imdb.com/"
	# http://www.imdb.com/list/ls006266261/
	# http://www.imdb.com/list/ls006266261/?nstart=1&view=compact&sort=listorian:asc&defaults=1&scb=0.11189682455768879
	start_urls = [  "http://www.imdb.com/list/ls006266261/?nstart=1&view=compact&sort=listorian:asc&defaults=1&scb=0.11189682455768879"]

					# "http://www.imdb.com/list/ls006266261/?start=251&view=compact&sort=listorian:asc",
					# "http://www.imdb.com/list/ls006266261/?start=501&view=compact&sort=listorian:asc",
					# "http://www.imdb.com/list/ls006266261/?start=751&view=compact&sort=listorian:asc" ]

	def parse(self, response):
		# rows = response.xpath("//div/div/div/div/div/div/div/table/tbody")       
		rows = response.xpath('//div/div/div/div/div/div/div/table/tbody/tr/td')

		movies = []
		print("\n\n\n\n\n\nROW")
		print(rows)
		print("\n\n\n\n\n\n")
		
		for row in rows:
			movie = collections.OrderedDict()
			movie['title'] = row.xpath("//div/div/div/div/div/div/div/table/tbody/tr[@class='list_item']/td[@class='title']/a/text()").extract()
			movie['url'] = row.xpath("//div/div/div/div/div/div/div/table/tbody/tr[@class='list_item']/td[@class='title']/a/@href")[0].extract()
			movie['year'] = row.xpath("//div/div/div/div/div/div/div/table/tbody/tr[@class='list_item']/td[@class='year']/text()").extract()
			print("\n\n\n\n\n\n\n\n\n\n\nhi")
			print(movie)
			print("\n\n\n\n\n\n\n\n\n\n\nhi")
			movies.append(movie)
			# req = Request(allowed_domains.append(movie['url']), callback=self.LinkParse)
			# req.meta['movie_info'] = movie
			# ans.append(req)

		return movies
		


	def LinkParse(self, response):
		mov = response.meta['movie_info']
		info = response.xpath("//div/div/div/div/div/div/div/div/div/div/div/div[@class='title_wrapper']/div[@class='subtext']").extract()
		synopsis = response.xpath("//div/div/div/div/div/div/div[@class='inline canwrap']/p/text()").extract()	
		mov['synopsis'] = synopsis
		return mov       



# //div/div/div/div/div/div/div/table/tbody/tr/td


# # show 100
# //div/div/div/div/div/div/div/div/div/b

# # show 250 - TITLE
# //div/div/div/div/div/div/div/table/tbody/tr/td[@class='title']/a/text()

# YEAR
# //div/div/div/div/div/div/div/table/tbody/tr/td[@class='year']/text()




# MOVIE LINK
# //div/div/div/div/div/div/div/div/div/div/div/div/div[@class='subtext']

# MOVIE STORYLINE
# //div/div/div/div/div/div/div[@class='inline canwrap']/p/text()

# MOVIE INFO
# //div/div/div/div/div/div/div/div/div/div/div/div[@class='title_wrapper']/div[@class='subtext']

# //div/div/div/div/div/div/div/table/tbody/tr[@class='list_item']/th

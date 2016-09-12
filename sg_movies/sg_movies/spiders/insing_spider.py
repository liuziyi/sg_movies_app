import scrapy

from sg_movies.items import SgMoviesItem

class inSingSpider(scrapy.Spider):
	name = "inSing"
	allowed_domains = ["insing.com"]
	start_urls = ["http://www.insing.com/movies/now-showing/"]

	def parse(self, response):
		for href in response.css('section.module-movie-grid-list > ul > li > figure > a::attr("href")'):
			url = response.urljoin(href.extract())
			yield scrapy.Request(url, callback=self.parse_contents)

	def parse_contents(self, response):
		for sel in response.xpath('//div[@class="left-main"]'):
			item = SgMoviesItem()
			item['title'] = sel.xpath('section[@class="module-movie-info container"]/div/ul/li/div[@class="movie-title"]/h1/text()').extract()[0]
			item['duration'] = sel.xpath('section[@class="module-movie-info container"]/div/ul/li/div[@class="rated"]/div[@itemprop="contentRating"]/time/text()').extract()[0]
			item['genre'] = sel.xpath('section[@class="module-movie-info container"]/div/ul/li/div[@class="genre"]/div[@itemprop="genre"]/text()').extract()[0]
			item['lang'] = sel.xpath('section[@class="module-movie-info container"]/div/ul/li/div[@class="lang"]/div[@itemprop="subtitleLanguage"]/text()').extract()[0]
			item['opening'] = sel.xpath('section[@class="module-movie-info container"]/div/ul/li/div[@class="cinema"]/div[@itemprop="datePublished"]/text()').extract()[0]
			item['rating'] = sel.xpath('section[@class="module-movie-info container"]/div/ul/li/div[@class="rated"]/div[@itemprop="contentRating"]/text()').extract()[0]
			item['synopsis'] = sel.xpath('section[@class="movie-plot panel container"]/div/p/text()').extract()[0]
			item["poster"] = sel.xpath('section[@class="module-movie-info container"]/figure/img/@src').extract()[0]
			yield item


from scrapy.spiders import BaseSpider
from example_bot.items import ExampleDotComItem

class ExampleSpider(BaseSpider):
    name = "example"
    allowed_domains = ["example.com"]
    start_urls = ['http://www.example.com/']

    def parse(self, response):
         title = response.xpath('//title/text()').extract()[0]
         description = response.xpath('//body/div/p/text()').extract()[0]
         return ExampleDotComItem(title=title, description=description)



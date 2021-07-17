import scrapy


class YahoofinanceSpider(scrapy.Spider):
    name = 'yahooFinance'
    allowed_domains = ['https://finance.yahoo.com']
    start_urls = ['http://https://finance.yahoo.com/']

    def parse(self, response):
        pass

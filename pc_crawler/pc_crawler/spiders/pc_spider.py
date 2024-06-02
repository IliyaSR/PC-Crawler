import scrapy


class PcSpiderSpider(scrapy.Spider):
    name = "pc_spider"
    allowed_domains = ["desktop.bg"]
    start_urls = ["https://desktop.bg/computers-all"]

    def parse(self, response):
        pass

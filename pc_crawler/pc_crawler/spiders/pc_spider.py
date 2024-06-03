import scrapy

from ..items import PcCrawlerItem


class PcSpiderSpider(scrapy.Spider):
    name = "pc_spider"
    allowed_domains = ["desktop.bg"]
    start_urls = ["https://desktop.bg/computers-all"]

    def parse(self, response):
        all_computers = response.css('ul.products li article a::attr(href)').getall()

        for url_computer in range(0, len(all_computers), 2):
            yield scrapy.Request(all_computers[url_computer], callback=self.parse_computer)

        next_page = response.xpath('//a[@rel="next"]/@href').get()

        if next_page is not None:
            next_page_url = response.urljoin(next_page)
            yield scrapy.Request(next_page_url, callback=self.parse)

    def parse_computer(self, response):
        table_rows = response.css('table tr')
        item = PcCrawlerItem()
        item['processor'] = table_rows[6].css('td ::text').get()
        item['gpu'] = table_rows[7].css('td ::text').get()
        item['motherboard'] = table_rows[5].css('td ::text').get()
        if table_rows[8].css('td label span::text').get() is not None:
            item['ram'] = table_rows[8].css('td label span::text').get().strip()
        else:
            item['ram'] = table_rows[8].css('td ::text').get()
        yield item

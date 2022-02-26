import scrapy
class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['http://192.168.63.167/snow']
    def parse(self,response):
        css_selector = 'img'
        for x in response.css(css_selector):
            newsel = '@src'
            yield {
                'image link': x.xpath(newsel).extract_first(),
            }

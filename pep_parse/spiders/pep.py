import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for pep_link in response.css('#numerical-index a.pep.reference.internal::attr(href)'):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        page_title = response.css('h1.page-title::text')
        data = dict(
            number=page_title.get().split()[1],
            name=page_title.get(),
            status=response.css('abbr::text').get(),)
        yield PepParseItem(data)

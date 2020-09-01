import scrapy


class LatestUpdatesSpider(scrapy.Spider):
    name = 'mangakatana-updates'

    start_urls = [
        'http://mangakatana.com/',
    ]

    page = 2

    def parse(self, response):
        books = []
        for book in response.css('div#book_list > div.item'):
            yield {
                'title': book.css('h3.title a::text').get()
            }

        next_page = response.css('li > a.next.page-numbers::attr(href)').get()

        while self.page <= 4:
            next_page = response.urljoin(f'http://mangakatana.com/page/{self.page}')
            yield scrapy.Request(next_page, callback=self.parse)
            self.page += 1
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
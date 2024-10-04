import scrapy

class JcrewDressesSpider(scrapy.Spider):
    name = 'womens_dresses'
    start_urls = [
        'https://www.jcrew.com/plp/womens/categories/clothing/dresses-and-jumpsuits'
    ]

    def parse(self, response):
        # Extract the name of the dress
        urls = response.css('li[data-testid="product-tile"] a::attr(href)').getall()
        for url in urls:
            full_url = response.urljoin(url)
            yield scrapy.Request(full_url, callback=self.parse_product_details)

    def parse_product_details(self, response):
            yield {
                'name': response.css('h1[id="product-name__p"]::text').get().strip()
            }
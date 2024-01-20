import scrapy


class ScrapemeSpider(scrapy.Spider):
    name = "scrapeme"
    allowed_domains = ["scrapeme.live"]
    start_urls = ["https://scrapeme.live/shop/"]

    def parse(self, response):
        products = response.css(".product")
        for product in products:
            price_text_elements = product.css(".price *::text").getall()
            price = "".join(price_text_elements)
           
            yield {
                "name": product.css("h2::text").get(),
                "image": product.css("img").attrib["src"],
                "price": price,
                "url": product.css("a").attrib["href"],
            }

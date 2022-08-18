import scrapy
from ..items import AmazonscrapyItem


class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon_spider'
    page_number = 2
    start_urls = [
        'https://www.amazon.com/s?k=gaming+keyboard&pd_rd_r=dd3c0b5e-9ce2-4115-82a9-fde31b9532fa&pd_rd_w=buyKf&pd_rd_wg=RhCxH&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=8ZCRZ3R9N3H4SSMF1SCZ&qid=1660807312&ref=sr_pg_2'
    ]

    def parse(self, response):
        items = AmazonscrapyItem()

        product_name = response.css('.s-link-style .a-size-medium::text').extract()
        product_price = response.css('.a-price-whole::text').extract()
        product_image_link = response.css('.s-image::attr(src)').extract()

        items['product_name'] = product_name
        items['product_price'] = product_price
        items['product_image_link'] = product_image_link

        yield items

        next_page = 'https://www.amazon.com/s?k=gaming+keyboard&page=' + str(AmazonSpiderSpider.page_number) + '&pd_rd_r=dd3c0b5e-9ce2-4115-82a9-fde31b9532fa&pd_rd_w=buyKf&pd_rd_wg=RhCxH&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=8ZCRZ3R9N3H4SSMF1SCZ&qid=1660807312&ref=sr_pg_2'
        if AmazonSpiderSpider.page_number < 21:
            AmazonSpiderSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

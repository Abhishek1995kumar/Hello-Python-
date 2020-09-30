import requests
import scrapy
import lxml

class Amazon_Product(scrapy.Spider):

    name = 'amazon_reviews'
    domains = ['amazon.in']

    url = "https://www.amazon.com/s?k=amazonbasics&pf_rd_p=fef24073-2963-4c6b-91ab-bf7eab1c4cac&pf_rd_r=5CT1S65X1V9RP52ZPT5M"
    r = requests.get(url)
    amazon = r.content
    print(amazon)

    urls = []
    for i in range(1, 100):
        urls.append(url + str(i))

        def parse(self, resp):
            data = resp.css('#cm_cr-review_list')

            rating = data.css('.review-rating')

            comments = data.css('.review-text')
            count = 0

            scrapy_data = Amazon_Product()

            product_name = resp.css('.s-access-title :: text').extract()

            product_author = resp.css(
                '.a-color-secondary+ .a-color-secondary,#result () .a-color-secondary .a-text-normal').css(
                ':: text').extract()

            product_price = resp.css(
                '.a-spacing-none:nth child(2) .sx-price-fractional,.a-spacing-none:nth child(2) .sx-price-whole').css(
                ':: text').extract()

            product_imagelink = resp.css('.cfMarker :: attr(src)').extract()

            for fetch in rating:
                yield {'stars': ''.join(fetch.xpath('.//text()').extract()),
                       'comment': ''.join(comments[count].xpath(".//text()").extract())
                       }
                count += 1
            print(fetch)

            scrapy_data['product_name'] = product_name
            scrapy_data['product_author'] = product_author
            scrapy_data['product_price'] = product_price
            scrapy_data['product_name'] = product_imagelink

            yield {
                'product_name' : product_name,
                'product_author' : product_author,
                'product_price' : product_price,
                'product_imagelink' : product_imagelink
                }

            yield scrapy_data

            next_page = ('https://www.amazon.in/s?k=next+page&i=digital-text&page=2&qid=1598748091&ref=sr_pg_1 + str(Amazon_Product.page_numbers) + https://www.amazon.in/s?k=next+page&i=digital-text&page=2&qid=1598748091&ref=sr_pg_1')
            if Amazon_Product.page_number <= 100:
                Amazon_Product.page_number += 1
                yield resp.follow(next_page,call = self.parse)

Amazon = Amazon_Product()
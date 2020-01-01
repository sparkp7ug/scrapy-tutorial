import scrapy
import csv

class QuotesSpider(scrapy.Spider):
    name = "quotes_author"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]
    
    def parse(self, response):
        with open('quote_file.csv', mode='w') as quote_file:
            file_writer = csv.writer(quote_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['Quote','Author','Tags','Other'])
            for quote in response.css('div.quote'):
                #yield {
                #    'text': quote.css('span.text::text').get(),
                #    'author': quote.css('small.author::text').get(),
                #    'tags': quote.css('div.tags a.tag::text').getall(),
                #}
                file_writer.writerow([quote.css('span.text::text').get(),quote.css('small.author::text').get(),quote.css('div.tags a.tag::text').getall()])





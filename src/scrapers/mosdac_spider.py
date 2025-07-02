import scrapy
from bs4 import BeautifulSoup
import os

class MosdacSpider(scrapy.Spider):
    name = 'mosdac'
    allowed_domains = ['mosdac.gov.in']
    start_urls = ['https://www.mosdac.gov.in']

    def parse(self, response):
        # Extract main content
        content = response.css('main').extract_first()
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extract text content
        text = soup.get_text(separator=' ', strip=True)
        
        # Extract metadata
        metadata = {
            'title': response.css('title::text').get(),
            'meta_description': response.css('meta[name="description"]::attr(content)').get(),
            'url': response.url
        }
        
        yield {
            'content': text,
            'metadata': metadata,
            'html': content
        }

        # Follow links to other pages
        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)
import scrapy

from follow_alicate.items import CommentItem

class folhaSpider(scrapy.Spider):
    name = "folha"
    start_urls = [
        "http://comentarios1.folha.com.br/perfil/175843?skin=folhaonline"
    ]

    def parse(self, response):
        for sel in response.css('.comment_li'):
            item = CommentItem()
            yield item

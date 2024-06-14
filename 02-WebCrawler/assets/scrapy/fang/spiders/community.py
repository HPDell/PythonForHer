from typing import Any, Iterable
from time import sleep
from random import uniform
from scrapy import Spider, FormRequest
from scrapy.http import Request, Response
from scrapy.settings import BaseSettings
from fang.items import CommunityItem


class CommunityListSpider(Spider):
    name = "community_list"
    custom_settings = {
        "FEEDS": {
            "community_list.json": {
                "format": "json",
                "overwrite": False
            }
        }
    }

    start_urls = [
        "https://zz.esf.fang.com/housing/"
    ]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        for item in response.css("div.houseList div.list"):
            yield CommunityItem(
                name=item.css("a.plotTit::text").get(),
                link=item.css("a.plotTit::attr(href)").get(),
                category=item.css("span.plotFangType::text").get(),
                district=item.css("dd p:nth-of-type(2) a:nth-of-type(1)::text").get(),
                region=item.css("dd p:nth-of-type(2) a:nth-of-type(2)::text").get(),
                price_psm=item.css("p.priceAverage span::text").get()
            )
        pagers: list = response.css("div.fanye a")
        next_page = [p for p in pagers if len(p.re("下一页")) > 0]
        if len(next_page) > 0:
            sleep(1 + uniform(0, 1))
            next_page_link = next_page[0].css("::attr(href)").get()
            yield response.follow(next_page_link, callback=self.parse)

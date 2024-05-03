import scrapy
from scrapy.http import Response

from real_estate_scraper.items import RealEstateML
from datetime import datetime, timedelta


class SpiderForMlSpider(scrapy.Spider):
    name = "spider_for_ml"
    allowed_domains = ["lun.ua"]
    start_urls = ["https://lun.ua/uk/%D0%BD%D0%B5%D1%80%D1%83%D1%85%D0%BE%D0%BC%D1%96%D1%81%D1%82%D1%8C-"
                  "%D1%96%D0%B2%D0%B0%D0%BD%D0%BE-%D1%84%D1%80%D0%B0%D0%BD%D0%BA%D1%96%D0%B2%D1%81%D1%8C%D0%BA%D0%B0"
                  "?radius=30&order=popularity"]

    def parse(self, response: Response, **kwargs):
        detail_links = response.css("div.Card > a.Card-link::attr(href)").getall()

        yield from response.follow_all(detail_links, self.scrape_single_real_estate)

    def scrape_single_real_estate(self, response: Response) -> RealEstateML:
        return RealEstateML(
            name=self._scrape_name(response),
            statistic=self._scrape_statistic(response)
        )

    @staticmethod
    def _scrape_name(response: Response) -> str | None:
        if name := response.css(".BuildingContacts-header > h1::text").get():
            return name.strip("\n").strip()

        return None

    @staticmethod
    def _scrape_statistic(response: Response) -> dict | None:
        result = {}
        if statistics := response.css(".BuildingChart-column"):
            if len(statistics) >= 36:
                current_date = datetime.now()
                start_date = current_date - timedelta(days=36 * 30)

                for i, stat in enumerate(statistics[-36:], 1):
                    key_date = start_date + timedelta(days=i * 30)
                    key = key_date.strftime("%Y-%m")

                    value = stat.css(".BuildingChart-bar::attr(data-price)")[1].get()

                    result[key] = value

        return result if result else None


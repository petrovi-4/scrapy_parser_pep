import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = "pep"
    allowed_domains = ["peps.python.org"]
    start_urls = ["https://peps.python.org/"]

    def parse(self, response):
        """
        Метод для обработки начальной страницы, извлечения ссылок на PEP и
        перехода к каждой ссылке.

        Аргументы:
        - response: объект Response, содержащий HTML-ответ на запрос.

        Возвращает:
        Генератор объектов Request для каждой страницы PEP.
        """
        pep_hrefs = response.css(
            "section#numerical-index tr > td:nth-child(3) a"
        )
        for link in pep_hrefs:
            url = response.urljoin(link.attrib["href"]) + "/"
            yield response.follow(url, callback=self.parse_pep)

    def parse_pep(self, response):
        """
        Метод для обработки страницы PEP и извлечения информации о номере,
        имени и статусе PEP.

        Аргументы:
        - response: объект Response, содержащий HTML-ответ на запрос.

        Возвращает:
        Генератор объектов PepParseItem с данными PEP.
        """
        number, name = (
            response.css("h1.page-title::text").get().split(" – ", 1)
        )
        pep_data = {
            "number": number.split()[1],
            "name": name,
            "status": response.css("abbr::text").get(),
        }
        yield PepParseItem(pep_data)

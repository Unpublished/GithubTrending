"""
A scraper for github's trending pages based on maniac103's script
"""
import scrapy


class TrendingSpiderBase(scrapy.Spider):
    timeRange = ""

    def start_requests(self):
        yield scrapy.Request(url='https://github.com/trending?since=' + self.timeRange, callback=self.parse)

    def parse(self, response):
        repo_list = response.css(".repo-list")
        for item in repo_list[0].css("li"):
            yield {
                'owner':       item.xpath("div/h3/a/span/text()").re(r'[^\s\/]*')[0],
                'repo':        self.to_string(item.xpath("div/h3/a/text()[2]")),
                'description': self.to_string(item.xpath("div[3]/p/text()")),
                'language':    self.to_string(item.xpath("div[4]/span/span[@itemprop='programmingLanguage']/text()")),
                'stars':       self.to_int(item.xpath("div[4]/a[1]/text()[2]")),
                'forks':       self.to_int(item.xpath("div[4]/a[2]/text()[2]")),
                'new_stars':   self.to_int(item.xpath("div[4]/span[@class='d-inline-block float-sm-right']/text()"))
            }

    @staticmethod
    def to_int(sel):
        if not sel:
            return 0
        return int("".join(sel.re(r'\d')))

    @staticmethod
    def to_string(sel):
        for value in sel.extract():
            if not value:
                continue
            stripped = value.strip()
            if len(stripped) > 0:
                return stripped
        return None


class DailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-all"
    timeRange = "daily"


class WeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-all"
    timeRange = "weekly"


class MonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-all"
    timeRange = "monthly"

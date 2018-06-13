"""
A scraper for github's trending pages based on maniac103's script
"""
import scrapy


class TrendingSpiderBase(scrapy.Spider):
    lang = "all"
    timeRange = ""

    def start_requests(self):
        url = 'https://github.com/trending/{lang}?since={range}'.format(lang=self.lang, range=self.timeRange)
        yield scrapy.Request(url=url, callback=self.parse)

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


class CPlusPlusDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-c++"
    lang = "c++"
    timeRange = "daily"


class CPlusPlusWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-c++"
    lang = "c++"
    timeRange = "weekly"


class CPlusPlusMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-c++"
    lang = "c++"
    timeRange = "monthly"


class HTMLDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-html"
    lang = "html"
    timeRange = "daily"


class HTMLWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-html"
    lang = "html"
    timeRange = "weekly"


class HTMLMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-html"
    lang = "html"
    timeRange = "monthly"


class JavaDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-java"
    lang = "java"
    timeRange = "daily"


class JavaWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-java"
    lang = "java"
    timeRange = "weekly"


class JavaMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-java"
    lang = "java"
    timeRange = "monthly"


class JavaScriptDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-javascript"
    lang = "javascript"
    timeRange = "daily"


class JavaScriptWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-javascript"
    lang = "javascript"
    timeRange = "weekly"


class JavaScriptMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-javascript"
    lang = "javascript"
    timeRange = "monthly"


class PHPDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-php"
    lang = "php"
    timeRange = "daily"


class PHPWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-php"
    lang = "php"
    timeRange = "weekly"


class PHPMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-php"
    lang = "php"
    timeRange = "monthly"


class PythonDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-python"
    lang = "python"
    timeRange = "daily"


class PythonWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-python"
    lang = "python"
    timeRange = "weekly"


class PythonMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-python"
    lang = "python"
    timeRange = "monthly"


class RubyDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-ruby"
    lang = "ruby"
    timeRange = "daily"


class RubyWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-ruby"
    lang = "ruby"
    timeRange = "weekly"


class RubyMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-ruby"
    lang = "ruby"
    timeRange = "monthly"


class RustDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-rust"
    lang = "rust"
    timeRange = "daily"


class RustWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-rust"
    lang = "rust"
    timeRange = "weekly"


class RustMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-rust"
    lang = "rust"
    timeRange = "monthly"


class UnknownDailyTrendingSpider(TrendingSpiderBase):
    name = "trending_daily-unknown"
    lang = "unknown"
    timeRange = "daily"


class UnknownWeeklyTrendingSpider(TrendingSpiderBase):
    name = "trending_weekly-unknown"
    lang = "unknown"
    timeRange = "weekly"


class UnknownMonthlyTrendingSpider(TrendingSpiderBase):
    name = "trending_monthly-unknown"
    lang = "unknown"
    timeRange = "monthly"

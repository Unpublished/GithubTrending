from time import sleep

from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.http import TextResponse


class CustomRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        process_response = super().process_response(request, response, spider)
        if isinstance(process_response, TextResponse):
            repo_list = process_response.css(".repo-list")
            if repo_list.__len__() == 0 and not spider.crawler.stats.get_value('retry/max_reached', 0):
                sleep(45)
                return self._retry(request, 'dissect', spider) or process_response
        return process_response

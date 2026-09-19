from time import sleep

from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.http import TextResponse

from spiders.trending import REPO_LIST_PATH


class CustomRetryMiddleware(RetryMiddleware):

    def process_response(self, request, response, **kwargs):
        process_response = super().process_response(request, response, **kwargs)
        if isinstance(process_response, TextResponse):
            repo_list = process_response.css(REPO_LIST_PATH)
            if repo_list.__len__() == 0:
                if self.crawler.stats and not self.crawler.stats.get_value('retry/max_reached', 0):
                    sleep(45)
                    return self._retry(request, 'dissect') or process_response
        return process_response

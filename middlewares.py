from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.http import TextResponse


class CustomRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        process_response = super().process_response(request, response, spider)
        if isinstance(process_response, TextResponse):
            repo_list = process_response.css(".repo-list")
            if repo_list.__len__() == 0:
                return self._retry(request, 'dissect', spider) or response
        return process_response

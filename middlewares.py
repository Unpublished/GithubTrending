from scrapy.downloadermiddlewares.retry import RetryMiddleware


class CustomRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        process_response = super().process_response(request, response, spider)
        repo_list = response.css(".repo-list")
        if repo_list.__len__() == 0:
            return self._retry(request, 'dissect', spider)
        return process_response

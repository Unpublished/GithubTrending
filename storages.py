import os

from io import BytesIO
from scrapy.extensions.feedexport import FileFeedStorage


class OverwriteStorage(FileFeedStorage):

    def open(self, spider):
        return BytesIO()

    def store(self, file):
        value = file.getvalue()
        if not value:
            file.close()
            return

        dirname = os.path.dirname(self.path)
        if dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        # changed from 'ab' to 'wb' to truncate file when it exists
        real_file = open(self.path, 'wb')
        real_file.write(value)
        file.close()
        real_file.close()

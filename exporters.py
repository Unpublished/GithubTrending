from collections import OrderedDict

from scrapy.exporters import JsonItemExporter
from scrapy.utils.python import to_bytes


class OrderedJsonItemExporter(JsonItemExporter):

    def export_item(self, item):
        if self.first_item:
            self.first_item = False
        else:
            self.file.write(b',')
            self._beautify_newline()
        itemdict = OrderedDict(self._get_serialized_fields(item))
        data = self.encoder.encode(itemdict)
        self.file.write(to_bytes(data, self.encoding))

from itemadapter import ItemAdapter


class PepParsePipeline:
    def process_item(self, item, spider):
        return item


class TotalPepPipeline:
    def process_item(self, item, spider):
        return item

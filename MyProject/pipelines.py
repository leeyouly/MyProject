# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from usda_gov.data import ImportUsdaInlandBasisStorage,ImportUsdaInlandBasisAddStorage
# from usda_gov.items import ImportUsdaInlandBasisItem,ImportUsdaInlandBasisAddItem
# from scrapy.utils.project import get_project_settings


class MyprojectPipeline(object):
    def process_item(self, item, spider):
        return item

'''
class UsdaInlandBasisSave(object):
    def __init__(self):
        self.storage = ImportUsdaInlandBasisStorage(get_project_settings().get('DATABASE'))

    def process_item(self, item, spider):
        if isinstance(item, ImportUsdaInlandBasisItem):
            if not self.storage.exist(item):
                self.storage.save_or_update(item)
                spider.crawler.stats.inc_value('spiderlog/save_count')
        return item
'''
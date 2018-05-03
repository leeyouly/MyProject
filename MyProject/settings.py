# -*- coding: utf-8 -*-

# Scrapy settings for dce project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MyProject'

SPIDER_MODULES = ['MyProject.spiders']
NEWSPIDER_MODULE = 'MyProject.spiders'

FTP_HOST = '192.168.8.234'
FTP_USER = 'ftp4dce'
FTP_PASSWORD = 'DCEftp123'
FTP_PATH = '/SYSTEM/product_wh/DceChicang'

ITEM_PIPELINES = {
    # 'ine.pipelines.ImportIcotton_Save': 300,
}
LOG_LEVEL = 'INFO'
JASONFILE_PATH='/u01/kettle_files/dce/'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
SPIDER_MIDDLEWARES = {
   'spiderlib.middlewares.IndexPageSaveMiddleware': 300,
}
EXTENSIONS = {
   'spiderlib.extensions.WriteEtlLog': 300,
}
DOWNLOAD_DELAY=1.5

DATABASE = 'oracle://stg:stg123@10.6.0.94:1521/?service_name=db'

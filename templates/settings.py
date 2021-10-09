from scrapy.get_image.ebookorg.ebookorg.settings import DOWNLOAD_DELAY, FEED_EXPORT_ENCODING, ROBOTSTXT_OBEY

FEED_EXPORT_ENCODING = 'utf-8'

DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'ja',
}
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'

ROBOTSTXT_OBEY  = False

DOWNLOAD_DELAY = 5

# images pipeline settings
ITEM_PIPELINES = {
    'ebookorg.pipelines.EbookorgPipeline': 300,
    #'scrapy.pipelines.images.ImagesPipeline': 400
    'ebookorg.pipelines.customImagePipeline': 400
}

IMAGES_STORE = '<path>'
IMAGES_URLS_FIELD = '<item field>'

# if you need to send request not parallel
CONCURRENT_REQUESTS = 1
DEPTH_PRIORITY = 1
SCHEDULER_DISK_QUEUE = "scrapy.squeues.PickleFifoDiskQueue"
SCHEDULER_MEMORY_QUEUE = "scrapy.squeues.FifoMemoryQueue"
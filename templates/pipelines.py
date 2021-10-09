#if you wanna change automatically naming feature for downloaded image file

from scrapy.pipelines.images import ImagePipeline

# override scrapy's naminig component here
class customImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        # process (ex: name = request.url.split('/')[-1])
        # process (ex: directory = item.get('title'))
        return 'path or file name'
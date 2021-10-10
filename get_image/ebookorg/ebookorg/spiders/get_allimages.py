import scrapy
from time import sleep
import re
import logging
from ebookorg.items import EbookorgItem
from scrapy.loader import ItemLoader
#import pprint

class GetImagesFromSearchSpider(scrapy.Spider):
    name = 'get_allimages'

    # Get target url and normalize it for scrapy here
    start_url = input("[*] Add url: ")
    input_domains = re.sub('org.+$', 'org', start_url.replace('https://', ''))
    allowed_domains = [input_domains]
    start_urls = [start_url]

    # We will add true title this assosiative array later
    # This assosiative array is used for a file path 
    global titles
    titles = {}

    global url_file_name
    file_name = input('[*] Add URL file name you need: ')
    url_file_name = f'ebookorg/url_files/{file_name}.txt'

    global downloaded_url_list
    try:
        with open(url_file_name, mode='r', encoding='utf-8') as f:
            print(f"[*] Found {file_name}.txt. loading....")
            downloaded_url_list = f.read().split('\n')
    except FileNotFoundError:
        with open(url_file_name, mode='w', encoding='utf-8') as f:
            print(f"[*] NotFound {file_name}.txt. make new file.")
            downloaded_url_list = [""]


    print('[*] Opened downloaded urls list')
    # This method is running on main page
    def parse(self, response):
        # Here process implement to go to images pages, and next main page  
        index_list = response.xpath('//div[@class="glink"]/../@href').getall()
        for images_page in index_list:
                yield response.follow(url=images_page, callback=self.parse_images)

        next = response.xpath('(//td[@class="ptds"]/following-sibling::td)[1]/a/@href').get()
        if next:
            self.wait_time
            yield response.follow(url=next, callback=self.parse)

    def parse_images(self, response):
        # Here process is judge this page is for japanese
        language = response.xpath('(//td[@class="gdt2"])[4]/text()').get()
        self.wait_time
        title_main = self.normalize_title(response.xpath('//h1[@id="gj"]/text()').get())
        if title_main == None:
            title_main = self.normalize_title(response.xpath('//h1[@id="gn"]/text()').get())
        
        # If this page is for Japanese, we get image URLs from this page
        if re.match(r'Japanese.*$', language):
            title_key = self.normalize_title(response.xpath('//h1[@id="gn"]/text()').get())
            # Correct title can't get from next image page, so we add it to title assosiative directory here
            titles[title_key] = title_main
            images = response.xpath('//div[@class="gdtm"]/div/a/@href').getall()

            print(f'[*] {title_main} is Japanese Page')
            print(f'[*] URL: {response.url}')
            # We got some embetted URLs from this page's images. so move there to get download URL for big size image
            for image in images:
                yield response.follow(url=image, callback=self.get_image)

            # If this page include some pages for image, we move there and callback this method to get all images
            next_images = response.xpath('(//td[@class="ptds"]/following-sibling::td)[1]/a/@href').get()
            if next_images:
                self.wait_time
                yield response.follow(url=next_images, callback=self.parse_images)
        else:
            print(f'[-] {title_main} is not Japanese Page')
            print(f'[-] URL: {response.url}')

    
    def get_image(self, response):
        if response.url not in downloaded_url_list:
            print('[*] This page has not downloaded yet')
            print(f'[*] target URL: {response.url}')
            # add collect title and image download URL to Item Loader
            # Item Loader send to Item Pipeline
            # Item Pipeline get image file from added URL and save it our local computer
            print('[*] get_image progress now')
            print(f'[*] target URL: {response.url}')
            self.wait_time
            title_key = self.normalize_title(response.xpath('//div[@id="i1"]/h1/text()').get())
            loader = ItemLoader(item=EbookorgItem(), response = response)
            loader.add_value('title', titles[title_key])
            loader.add_value('img_url',  response.xpath('//img[@id="img"]/@src').get())
            yield loader.load_item()
            self.current_url_to_downloaded_list(response.url)
        else:
            print('[-] This page has already downloaded. Skip.')
            print(f'[-] target URL: {response.url}')
        

    def current_url_to_downloaded_list(self, current_url):
        if current_url not in downloaded_url_list:
            with open(url_file_name, mode='a', encoding='utf-8') as f:
                print(current_url, file=f)
            print('[*] Current url write to downloaded url list')


    # when this method call, stop all process 
    # It is for data provider
    def wait_time(self):
        sleep(3)
    

    # We can customize title here
    def normalize_title(self, title):
        print(f'[*] in normalize progress: {title}')
        return title
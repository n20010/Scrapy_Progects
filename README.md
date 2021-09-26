# Summary
This repository include some my scrapy projects.<br>
[scrapy_tutorial](https://github.com/n20010/scrapy_projects/tree/main/scrapy_tutorial) is a archive repository I learned about scrapy.<br>
[get_image](https://github.com/n20010/scrapy_projects/tree/main/get_image) include some projects what is scrape images from actual website.<br>

# What is Scrapy
## [OFFICIALSITE](https://scrapy.org)
>An open source and collaborative framework<br> 
>for extracting the data you need from websites.<br>
>In a fast, simple, yet extensible way.<br>

# Usage
1. Get [Anaconda enviroment](https://www.anaconda.com/products/individual#Downloads)
2. Create virtual enviroment in Anaconda
    >You shuld select python3 version 3.8.<br>
    >2021/09 scrapy is not available on python3 ver3.9
3. Install some component need execute Scrapy in anaconda virtual enviroment

    ```Terminal
    pip install -r requirements.txt
    ```
4. [Install VScode](https://azure.microsoft.com/ja-jp/products/visual-studio-code/) in your local enviroment and add python extensions
5. clone this repository and move to project you need
    >If you use get_images project, you shuld to check IMAGES_STORE path in settings.py<br>
    >Images save to IMAGES_STORE, so it's need to chenge obey your enviroment<br>
6. Use this command, spider is execute.

    ```Terminal
    scrapy crawl <spider name you need>
    ```

# Main commands
  ## bench
  Execute simple benchmark test
  ```Terminal
  scrapy bench
  ```

  ## startproject
  Make new scrapy project
  ```Terminal
  scrapy startproject <project name>
  ```

  ## genspider
  Make new spider on currnt project<br>
  >(When type URL, remove 'https://' and last '/' is the best way)
  ```Terminal
  scrapy genspider (-t template name) <spider name> URL
  ```

  ## crawl
  Execute spider
  ```Terminal
  scrapy crawl <spider name>
  ```

  ## shell
  Execute scrapy shell<br>
  You can check Xpath, CSS etc...<br>
  ```Terminal
  scrapy shell
  ```
# Spetial Thanks
- [【3日で学べる】PythonでWebスクレイピング・クローリングを極めよう！（Scrapy、Selenium編）](https://www.udemy.com/course/python-web-scraping-with-scrapy/)
- [Scrapy Official Documents](https://docs.scrapy.org/en/latest/)
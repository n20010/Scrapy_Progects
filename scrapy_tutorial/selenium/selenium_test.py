from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('https://www.bing.com/')

search_bar = driver.find_element_by_id('sb_form_q')
search_bar.send_keys('python')
search_bar.send_keys(Keys.ENTER)

#search_btn = driver.find_element_by_xpath('//label[@for="sb_form_go"]')
#search_btn.click()
#search_btn.submit()


i = 0
while True:
    sleep(2) #二秒待つ
    for elem in driver.find_elements_by_xpath('//div[@class="b_title"]/h2/a'):
        print(elem.text)
        print(elem.get_attribute('href'))

    next_link = driver.find_element_by_xpath('//a[@title="次のページ"]')
    driver.get(next_link.get_attribute('href'))
    i += 1
    if i > 4:
        break

driver.close()
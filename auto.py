import time

from selenium import webdriver

url = 'https://www.youtube.com/'
driver = webdriver.Chrome(executable_path='./chromedriver')

try:
    driver.get(url=url)
    time.sleep(1)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()

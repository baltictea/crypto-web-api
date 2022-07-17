import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

URL = 'https://coinmarketcap.com/'


def get_top_100_list():
    driver = webdriver.Firefox()
    driver.get(URL)
    for _ in range(10):
        driver.execute_script('window.scrollTo(0, window.scrollY + 1000);')
        time.sleep(0.5)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table = soup.find('tbody')
    rows = table.find_all('tr')

    time_now = datetime.now().strftime('%I h %d-%m-%y')  # 1 h 23-04-05
    for i, row in enumerate(rows):
        columns = row.find_all('td')
        yield {
            'name': columns[2].find_all('p')[0].get_text(),
            'rate': columns[3].get_text().replace('$', '').replace(',', ''),
            'datetime': time_now
        }


def upload_data_to_api():
    for record in get_top_100_list():
        requests.post('http://127.0.0.1:8000/records', json=record)


upload_data_to_api()

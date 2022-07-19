import os.path
import time
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Скачиваем файл с помощью браузера
current_dir = current_directory = os.path.dirname(os.path.abspath(__file__))

options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": current_dir + '/tmp',
    "download.prompt_for_download": False,
}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.config.driver = driver

browser.open('https://demoqa.com/upload-download')
browser.element('#downloadButton').click()
time.sleep(1)

# Проверяем файл на его размер
assert os.path.getsize('tmp/sampleFile.jpeg') == 4096

# Удаляем файл из дирректории tmp
os.remove('tmp/sampleFile.jpeg')
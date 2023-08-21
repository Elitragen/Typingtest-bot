from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

words = []

url = "https://10fastfingers.com/typing-test/finnish"
driver.get(url)
time.sleep(3)

class_name = "CybotCookiebotDialogBodyButton"
element = driver.find_element(By.CLASS_NAME, class_name)
element.click()

# Wait for words to load
time.sleep(2)

# Locate the input field

input_field = driver.find_element(By.ID, "inputfield")
words_elements = driver.find_elements(By.CSS_SELECTOR, 'span[wordnr]')

for word in words_elements:
    input_field.send_keys(word.text)
    input_field.send_keys(Keys.SPACE)
    print(word.text)



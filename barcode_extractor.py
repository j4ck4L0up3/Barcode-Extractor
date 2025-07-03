#!/usr/bin/env python3
from selenium import webdriver
#from selenium.webdriver.chrome.options import Options
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# set options
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')

# initialize chrome driver
# uncomment stuff for options
# driver = webdriver.Chrome(options=chrome_options)
driver = webdriver.Chrome()

# open encoder page
driver.get('https://graphicore.github.io/librebarcode/documentation/code128.html')

input_text = 'Yippee!'
input_field = driver.find_element(By.CLASS_NAME, 'code128-encoder_input')

input_field.clear()
input_field.send_keys(input_text)

time.sleep(1)

output_field = driver.find_element(By.CLASS_NAME, "code128-encoder_output")
output_text = output_field.get_attribute('value')

print(output_text)

# wait 2 seconds
time.sleep(2)

# close browser window
driver.quit()
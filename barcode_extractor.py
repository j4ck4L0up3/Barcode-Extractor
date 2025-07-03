#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv

# set options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')

# initialize chrome driver
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# open encoder page
driver.get('https://graphicore.github.io/librebarcode/documentation/code128.html')

input_file = 'inventory.csv'
output_file = 'barcodes.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    csv_reader = csv.reader(infile, delimiter=',', quotechar='"')
    line_count = 0

    for row in csv_reader:
        if line_count != 0:

            input_text = ''.join(row)
            input_field = driver.find_element(By.CLASS_NAME, 'code128-encoder_input')

            input_field.clear()
            input_field.send_keys(input_text)

            time.sleep(1)

            output_field = driver.find_element(By.CLASS_NAME, "code128-encoder_output")
            output_text = output_field.get_attribute('value')

            outfile.write(output_text + '\n')
        
        line_count += 1

        # wait 2 seconds
        time.sleep(2)

# close browser window
driver.quit()


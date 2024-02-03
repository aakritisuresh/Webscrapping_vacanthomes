from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.select import Select
import pandas as pd
import requests
import time
import csv
import os

def write_to_file(row):
    with open('file.csv', 'a', newline='') as file:
       writer = csv.writer(file)
       writer.writerow(row)

def reset_file():
    # If such a file exists, delete it so we can recreate it.
    if os.path.exists('file.csv'):
        os.remove('file.csv')
    # Add header row to CSV file
    write_to_file(['Address', 'Date Condemned', 'Primary or Accessory*'])

def scrape_page(d):
    # Wrap this method in try/except because when d.find_element fails, it throws an error
    # In this case, some locations like "BELLONA-GITTINGS" returns "No results found" instead of the usual table
    try:
        tbody = d.find_element(By.ID, "ctl00_ContentPlaceHolder1_DataGrid1")
        for tr in tbody.find_elements(By.CSS_SELECTOR, 'tr:not(.headerrow)'):
            row = [item.text for item in tr.find_elements(By.TAG_NAME, 'td')]
            write_to_file(row)
    except:
        print('  No results found')

# extract table contents
def main():
    # debug auto-quit
    options = webdriver.ChromeOptions()
    # detach=True ensures that the chrome window stays open after this script completes processing
    # Helpful for debugging
    options.add_experimental_option("detach", False)

    service = Service(executable_path="/opt/homebrew/bin/chromedriver")
    # service = Service(executable_path="/Users/aakritisuresh/anaconda3/main.python.selenium/chromedriver-mac-x64/chromedriver")
    driver = webdriver.Chrome(options=options, service=service)

    # open url
    url = "https://cels.baltimorehousing.org/Search_DEM_Map.aspx"
    #ABELLE url = "https://cels.baltimorehousing.org/TL_DEM_Map.aspx"
    #ALLENDALE url = "https://cels.baltimorehousing.org/TL_DEM_Map.aspx"
    #ARCADIA url = "https://cels.baltimorehousing.org/TL_DEM_Map.aspx"
    base_url = driver.get(url)

    # select all neighbourhood placeholder
    select_element = Select(driver.find_element("id","ctl00_ContentPlaceHolder1_lstLoc"))

    # count the number of neighbourhoods
    all_neighbourhoods = select_element.options
    print(len(all_neighbourhoods))

    return_data = []
    i = 1

    reset_file()

    # Iterate over each neighborhood in select options
    for neighborhood in all_neighbourhoods:
        if neighborhood.get_attribute('value') == ' ':
            # Skip default empty value
            continue
        # Print each neighbourhood as you process it so if there is an error, we know which one to test
        print(i,' - ',neighborhood.get_attribute('value'))
        i+=1
        select_element.select_by_value(neighborhood.get_attribute('value'))

        # select Search Button
        search_button = driver.find_element('id','ctl00_ContentPlaceHolder1_btNB')
        search_button.click()
        # Add to existing list
        scrape_page(driver)
        # Go back to previous page with select options
        driver.back()

if __name__ == '__main__':  
    main()



# ?give url to soup package
# soup= BeautifulSoup(response,'html.parser' )
# print(soup)

# find all rows 
# data=soup.find('table').find('tbody').find_all('tr')


# Full Xpath of all row elements in the neighborhood page
#  /html/body/form/div[3]/div[2]/div[1]/div/table/tbody/tr/td/table[1]/tbody/tr[2]
#  /html/body/form/div[3]/div[2]/div[1]/div/table/tbody/tr/td/table[1]/tbody/tr[3]
#  /html/body/form/div[3]/div[2]/div[1]/div/table/tbody/tr/td/table[1]/tbody/tr[4]




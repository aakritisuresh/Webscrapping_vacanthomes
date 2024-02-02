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

# debug auto-quit
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(executable_path="/Users/aakritisuresh/anaconda3/main.python.selenium/chromedriver-mac-x64/chromedriver")
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

# select Neighborhood(by value
#ABELL = select_element.select_by_value("ABELL")

# select Neighbourhood(by Index)
select_element.select_by_index(1)

# extract all neighbourhood names
#for neighborhood in all_neighbourhoods:
#    print(neighborhood.text)

# select Search Button
search_button = driver.find_element('id','ctl00_ContentPlaceHolder1_btNB')  
search_button.click()

# url for new page
# response=driver.page_source


# extract table contents
def main():
    tbody = driver.find_element('xpath', '//*[@id="ctl00_ContentPlaceHolder1_DataGrid1"]')
    data = []
    for tr in row = tbody.find_elements(By.XPATH, '//tr'):
        row = [item.text for item in tr.find_elements(By.XPATH, './/tr')]
        data.append(row)
    print(data)

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




import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
import os

def chrome_driver():
    driver_path = ChromeDriverManager().install()
    print("Driver path:", driver_path)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode
    options.add_argument("--no-sandbox")  # Bypass OS security
    # Check if it's actually executable
    if not os.access(driver_path, os.X_OK):
        print("❌ Not executable. Trying to locate the real binary.")
        for root, dirs, files in os.walk(os.path.dirname(driver_path)):
            for file in files:
                if "chromedriver" in file and not file.endswith(".chromedriver"):
                    potential_path = os.path.join(root, file)
                    print("✅ Found likely candidate:", potential_path)
                    driver_path = potential_path
                    break

    return webdriver.Chrome(service=ChromeService(driver_path), options=options)


driver = chrome_driver()
# List to store extracted data
titles =[]
dates=[]
companies= []
locations =[]
salaries = []



# Target Url
url= "https://findajob.dwp.gov.uk/search?q=Data+Engineering+&loc=86383"

response = requests.get(url)

print(response.status_code)

driver.get(url)

# Allow page to load
time.sleep(11)

source_code = driver.page_source

soup = BeautifulSoup(response.content, 'html.parser')

#Extract data from each job card

job_openings = soup.find_all('div' ,class_="search-result")
for job in job_openings:
    #titles list
    title = job.find('h3').text.strip() if job.find else None
    titles.append(title)
    
    #Detail list
    details=job.find('ul' , class_= "search-result-details")
    li_items = details.find_all('li') if details else []

    # dates 
    date = li_items[0].text.strip() if len(li_items)>0 else None 
    dates.append(date)

    #companies and locations

    if len(li_items)>1:
        company_tag = li_items[1].find('strong')
        location_tag = li_items[1].find('span')
        companies.append(company_tag.text.strip()if company_tag else None)
        locations.append(location_tag.text.strip()if location_tag else None)

    else:
        companies.append(None)
        locations.append(None)

        #for salaries

    if len(li_items)>2:
        salary_tag = li_items[2].find ('strong')
        salaries.append(salary_tag.text.strip()if salary_tag else None)

    else:
        salaries.append(None)


print(titles)
print(dates)
print(companies)
print(locations)
print(salaries)

#create DataFrame

df = pd.DataFrame({
     "title" :titles,
     "date" : dates,
     "company":companies,
     "location":locations,
     "salary" :salaries, 


})

#save output
df.to_csv("djobs.csv",index=False)
print("CSV file updated successfully!")

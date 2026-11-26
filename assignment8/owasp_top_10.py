# Task 6: Scraping Structured Data

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://top10.owasp.org/2025/"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get(URL)

    xpath = '//h3[@id="top-102025-list"]/following-sibling::ol[1]/li/a'
    links = driver.find_elements(By.XPATH, xpath)

    vulnerabilities = [
        {
            "Title": " ".join(link.text.split()),
            "Href": link.get_attribute("href"),
        }
        for link in links
    ]

    print(vulnerabilities)

    df = pd.DataFrame(vulnerabilities)
    df.to_csv("owasp_top_10.csv", index=False)

finally:
    driver.quit()
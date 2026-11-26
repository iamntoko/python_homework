# Task 3: Write a Program to Extract this Data

import json

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://books.toscrape.com/"

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get(URL)

    book_elements = driver.find_elements(By.CSS_SELECTOR, "article.product_pod")
    print(f"Found {len(book_elements)} book elements")

    results = []

    for book in book_elements:
        title_link = book.find_element(By.CSS_SELECTOR, "h3 a")
        title = title_link.get_attribute("title")

        price = book.find_element(By.CSS_SELECTOR, "p.price_color").text.strip()

        rating_el = book.find_element(By.CSS_SELECTOR, "p.star-rating")
        rating_classes = rating_el.get_attribute("class").split()
        rating = next(
            (cls for cls in rating_classes if cls != "star-rating"),
            "Unknown",
        )

        results.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
        })

    df = pd.DataFrame(results)
    print(df)

finally:
    driver.quit()
    
    
# Task 4: Write out the Data

df.to_csv("get_books.csv", index=False)

with open("get_books.json", "w", encoding="utf-8") as json_file:
    json.dump(results, json_file, indent=2, ensure_ascii=False)
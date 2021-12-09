from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import os

service = Service("YOUR LOCAL FILE")
driver = webdriver.Chrome(service=service)

driver.get("URL")

heading = driver.find_element(By.ID, "chapter-heading")
content = driver.find_element(By.CLASS_NAME, "reading-content")
images = content.find_elements(By.TAG_NAME, "img")

image_urls = []
for image in images:
    image_urls.append(image.get_attribute("data-src").strip("\t\n"))

image_path = f"./{heading.text}"
os.mkdir(image_path)

n = 1
for url in image_urls:
    response = requests.get(url)
    with open(f"{image_path}/page-{n}.jpg", "wb") as file:
        file.write(response.content)
        n += 1

driver.quit()

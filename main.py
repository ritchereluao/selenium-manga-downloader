from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
import img2pdf
from natsort import natsorted
from glob import glob
import os

service = Service("LOCAL FILE")
driver = webdriver.Chrome(service=service)

driver.get(f"https://ww1.horimiya.net/manga/my-hero-academia-manga-chapter-318/")

heading = driver.find_element(By.ID, "chapter-heading")
content = driver.find_element(By.CLASS_NAME, "reading-content")
images = content.find_elements(By.TAG_NAME, "img")

image_urls = []
for image in images:
    image_urls.append(image.get_attribute("data-src").strip("\t\n"))

images_path = f"./{heading.text}"
os.mkdir(images_path)

n = 1
for url in image_urls:
    response = requests.get(url)
    with open(f"{images_path}/page-{n}.jpg", "wb") as file:
        file.write(response.content)
        n += 1

with open(f"{heading.text}.pdf", "wb") as file:
    file.write(img2pdf.convert(natsorted(glob(f"{images_path}/*.jpg"))))

driver.quit()

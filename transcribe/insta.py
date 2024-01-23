from fileinput import filename
from bs4 import BeautifulSoup
from selenium import webdriver
from uuid import uuid4
import re
import requests
# from playwright.sync_api import Page, expect
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
import os

PATH = "research/edge drivers/msedgedriver"
print(
    os.path.exists(PATH)
)

reg1= pattern = '"mimeType="audio\\/mp4" [a-zA-Z="0-9 _><:/\\.]+BaseURL>[a-zA-Z="0-9 _><:/\\.?&;%-]+<\\'
reg2= '"mimeType="audio\\/mp4" [a-zA-Z="0-9 _><:/\\.]+BaseURL>'

def extract_url_from_source(html_content: str):
    base_url= ""
    print(type(html_content))
    # soup= BeautifulSoup(html_content, "html.parser")
    # for script in soup.body.find_all("script"):
        # contents= script.contents
    contents= [html_content]
    soup= BeautifulSoup(html_content, "xml")
    
    for script in soup.body.find_all("script"):
        contents= script.contents
    
    with open("media/ut.html", "w") as f:
        f.write(html_content)
        
headers= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \
    Safari/537.36 Edg/79.0.309.43",
    # "cookie": f'sessionid={SESSIONID};'
}
       

def extract_video_from_url(url, mp4_filename):
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=True, channel="msedge")
    page = browser.new_page()
    page.goto(url)
    page_source = page.content()
    base_url = extract_url_from_source(page_source,)
    response= requests.get(base_url,headers=headers)
    if response.status_code == 200:
        filename= f"media/{uuid4().__str__()}.mp4"
        with open(mp4_filename, "wb") as f:
            f.write(
                response.content
            )
    return mp4_filename

url = "https://www.instagram.com/reel/C2bjQ6CLMY3/?igsh=cnZqeWV1cXdraWZ6"
mp4_filename = "output.mp4"
filename = extract_video_from_url(url, mp4_filename)
print(f"file created is : {filename}")











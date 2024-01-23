from bs4 import BeautifulSoup
from selenium import webdriver
from uuid import uuid4
import re
import requests
# from playwright.sync_api import Page, expect
import asyncio
from playwright.async_api import async_playwright
from playwright.sync_api import sync_playwright
from datetime import datetime


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


            
            







def extract_video_from_url(url, mp4_filename):
    playwright = sync_playwright().start()
    
    browser = playwright.chromium.launch(headless=True, channel="msedge")
    page = browser.new_page()    
    page.goto(url)
    
    content = page.content()
    file_name= f"media/{uuid4().hex}.html"
    
    with open(file_name, "w") as f:
        f.write(content)
    print(file_name)
    

url = "https://www.instagram.com/reel/Cz_IOtkoSo6/"

mp4_filename="output.mp4"

extract_video_from_url(url,mp4_filename)


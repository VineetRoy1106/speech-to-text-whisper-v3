import os
import requests
from uuid import uuid4
from bs4 import BeautifulSoup
from playwright.async_api import async_playwright
playwright =  async_playwright().start()

# async def download_video(url):
#     # Start Playwright
#     playwright = await async_playwright().start()

#     try:
#         # Launch Chromium browser
#         browser = await playwright.chromium.launch(headless=True, channel="msedge")
#         page = await browser.new_page()

#         # Navigate to the specified URL
#         await page.goto(url)

#         # Get page content
#         content = await page.content()

#         # Parse HTML content
#         soup = BeautifulSoup(content, 'html.parser')

#         # Find video tag and extract video URL
#         video_tag = soup.find('video')
#         if video_tag:
#             video_url = video_tag['src']

#             # Download the video using requests
#             video_response = requests.get(video_url)

#             # Check if the video download was successful
#             if video_response.status_code == 200:
#                 # Create 'media' directory if it doesn't exist
#                 os.makedirs('media', exist_ok=True)

#                 # Generate a unique filename for the video
#                 filename = f"media/{uuid4()}.mp4"

#                 # Save the video to the 'media' directory
#                 with open(filename, 'wb') as file:
#                     file.write(video_response.content)

#                 print(f'File downloaded successfully. Saved as: {filename}')
#             else:
#                 print('Failed to download video.')
#         else:
#             print('Video tag not found on the page.')

#     finally:
#         # Close the browser and stop Playwright
#         await playwright.stop()

# # Example usage:
# url_to_scrape = "https://www.instagram.com/reel/Cz_IOtkoSo6"
# await download_video(url_to_scrape)

import os
import requests
from uuid import uuid4
from bs4 import BeautifulSoup
import asyncio
from playwright.async_api import async_playwright

# async def download_video(url):
#     # Start Playwright
#     playwright = await async_playwright().start()

#     try:
#         # Launch Chromium browser
#         browser = await playwright.chromium.launch(headless=True, channel="msedge")
#         page = await browser.new_page()

#         # Navigate to the specified URL
#         await page.goto(url)

#         # Get page content
#         content = await page.content()

#         # Parse HTML content
#         soup = BeautifulSoup(content, 'html.parser')

#         # Find video tag and extract video URL
#         video_tag = soup.find('video')
#         if video_tag:
#             video_url = video_tag['src']

#             # Download the video using requests
#             video_response = requests.get(video_url)

#             # Check if the video download was successful
#             if video_response.status_code == 200:
#                 # Create 'media' directory if it doesn't exist
#                 os.makedirs('media', exist_ok=True)

#                 # Generate a unique filename for the video
#                 filename = f"media/{uuid4()}.mp4"

#                 # Save the video to the 'media' directory
#                 with open(filename, 'wb') as file:
#                     file.write(video_response.content)

#                 print(f'File downloaded successfully. Saved as: {filename}')
#             else:
#                 print('Failed to download video.')
#         else:
#             print('Video tag not found on the page.')

#     finally:
#         # Close the browser and stop Playwright
#         await playwright.stop()

# # Example usage:
# async def main():
#     url_to_scrape = "https://www.instagram.com/reel/Cz_IOtkoSo6"
#     await download_video(url_to_scrape)

# # Run the asynchronous function using asyncio.run
# if __name__ == "__main__":
#     asyncio.run(main())

import os
import requests
from uuid import uuid4
from bs4 import BeautifulSoup
import asyncio
from playwright.sync_api import sync_playwright

def inspect_network_tab(url):
    playwright = sync_playwright().start()
    print('start')
    browser = playwright.chromium.launch( )
    print('got started')
    page = browser.new_page()
    page.goto(url)

       
    page.keyboard.press('Control+Shift+I')  # Shortcut for opening DevTools
    print('inspected')
    
    print('ready to open network')
    page.keyboard.press('Control+Shift+D')  # Shortcut for switching to the "Network" tab
    print('network opened')
    
    filter_box = page.locator("text=Filter")
    filter_box.fill("mp4")
    page.keyboard.press("Enter")
    
    print("mp4 searched")
    
    

    # Perform actions in the Network tab (example)
    last_request =  page.wait_for_selector('.network-request:last-child')
    print('last fetched')

    # Perform your actions on the last network request
    print("Last network request URL:",last_request.get_attribute('title'))

    input("Press Enter to close the browser...")  # Keep the browser open for inspection
    response = page.wait_for_response()
    print(f"Response status code: {response.status}") 

# # Example usage:
url_to_scrape = "https://www.instagram.com/reel/Cz_IOtkoSo6"
inspect_network_tab((url_to_scrape))

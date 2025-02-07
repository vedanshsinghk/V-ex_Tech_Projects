import requests
from bs4 import BeautifulSoup

def scrape_titles(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.find_all('h1')
    for title in titles:
        print(title.text)

url = input("Enter the URL to scrape: ")
scrape_titles(url)

# python -m venv myenv
# myenv\Scripts\activate  # On Windows
# pip install beautifulsoup4

# (myenv) D:\Internship\Python Basics\DAY9\simple_web_scraper>

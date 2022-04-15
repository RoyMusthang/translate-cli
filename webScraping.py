import time
import requests
import selenium import webdriver
from selenium.webdriver.firefox.options import Options
import json
from bs4 import BeautifulSoup


def make_requests(url):
    response = requests.get(url)
    return response.content


def main():
    url = 'https://translate.google.com/?sl=pt&tl=en&op=translate'
    print(make_requests(url))

if __name__ == '__main__':
    main()
    

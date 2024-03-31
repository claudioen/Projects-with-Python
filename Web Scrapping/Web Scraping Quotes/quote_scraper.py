import requests
from bs4 import BeautifulSoup

def scrape_quotes():
    base_url = 'http://quotes.toscrape.com'
    next_page = '/page/1/'

    while next_page:
        url = base_url + next_page
        response = requests.get(url)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            quotes = soup.find_all('div', class_='quote')
            
            for quote in quotes:
                text = quote.find('span', class_='text').text
                author = quote.find('small', class_='author').text
                print(f'"{text}" - {author}')
            
            next_button = soup.find('li', class_='next')
            next_page = next_button.find('a')['href'] if next_button else None
        else:
            print('Failed to retrieve page.')

if __name__ == "__main__":
    scrape_quotes()

import requests
from bs4 import BeautifulSoup
URL = "https://www.sciencedirect.com/browse/journals-and-books?subject=environmental-science"


def get_html_page():
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/92.0.4515.159 Safari/537.36',
        'referer': 'https://...'
    }
    response = requests.get(URL, headers=headers)
    print(response.status_code)
    if response:
        return response.text
    else:
        return None


def get_articles():
    res_page = get_html_page()
    if res_page:
        soup = BeautifulSoup(res_page, 'html.parser')
        print(type(soup))
        ol = soup.ol
        articles = ol.find_all('li', {'class': 'publication branded u-padding-xs-ver js-publication'})
        articles = [article.a.span.string for article in articles]
        [print(article) for article in articles]


if __name__ == '__main__':
    get_articles()

from bs4 import BeautifulSoup
import requests
URL = "http://recurship.com/"


def html_page(url):

    response = requests.get(url)
    if response:
        return response.text
    else:
        return None


def get_links():

    res_page = html_page(URL)
    if res_page:
        soup = BeautifulSoup(res_page, 'html.parser')
        articles = soup.find_all('article')
        links = [link.header.h2.a['href'] for link in articles]
        return links
    else:
        print("Restricted Url")
        return None


def scraper():
    links = get_links()
    if links:
        results = {}
        for link in links:
            res_page = html_page(link)
            if res_page:
                soup = BeautifulSoup(res_page, 'html.parser')

                images = soup.find_all('img')
                src = [image['src'] for image in images]
                results[soup.title.string] = src
        return results
    else:
        return None


if __name__ == '__main__':
    results = scraper()
    if results:
        for key in results:
            print("{", key, ":", results[key], "}")

import requests
from bs4 import BeautifulSoup

headers: dict = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://www.ebay.com/',
    'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}


def get_total_pages() -> int:
    total_pages: list = []
    params: dict = {
        '_from': 'R40',
        '_trksid': 'p2380057.m570.l1313',
        '_nkw': 'iphone'.replace(' ', '+'),
        '_sacat': '0',
    }

    url: str = 'https://www.ebay.com/sch/i.html?'
    res = requests.get(url=url, params=params, headers=headers)
    f = open('temp/res.html', 'w+')
    f.write(res.text)
    f.close()

    # scraping process
    soup = BeautifulSoup(res.text, 'html.parser')
    pagination = soup.find('nav', attrs={'class': 'pagination'})
    pages = pagination.find_all('li')
    for item in pages:
        paginate = item.find('a').text.strip()
        total_pages.append(int(paginate))

    # get max total Pages
    total: int = max(total_pages)
    print(f'Total page found: {total}')
    return total


def get_all_items():
    params: dict = {
        '_from': 'R40',
        '_trksid': 'p2380057.m570.l1313',
        '_nkw': 'iphone'.replace(' ', '+'),
        '_sacat': '0',
    }

    url: str = 'https://www.ebay.com/sch/i.html?'
    res = requests.get(url=url, params=params, headers=headers)
    f = open('temp/res.html', 'w+')
    f.write(res.text)
    f.close()

    # scraping process
    soup: BeautifulSoup = BeautifulSoup(res.text, 'html.parser')
    srp_result = soup.find('ul', attrs={'class': 'srp-results srp-list clearfix'})
    contents = srp_result.find_all('li', attrs={'class': 's-item s-item__sep-on-bottom'})
    for content in contents:
        title = content.find('h3', attrs={'class': 's-item__title'}).text
        image = content.find('img', attrs={'class': 's-item__image-img'})['src']
        link = content.find('a', attrs={'class': 's-item__link'})['href']
        price = content.find('span', attrs={'class': 's-item__price'}).text.strip()
        print(price)


if __name__ == '__main__':
    get_all_items()

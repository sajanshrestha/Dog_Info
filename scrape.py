import requests
from bs4 import BeautifulSoup

base_url = 'https://www.purina.com'


def get_all_links(url):
    ''' gets all the links from the current page '''

    html = requests.get(url).text
    bs_obj = BeautifulSoup(html, 'lxml')

    links = (link.attrs['href'] for link in bs_obj.findAll(
        'a', attrs={'class': 'link'}) if 'href' in link.attrs)
    return links


def get_info(url):
    ''' goes to the link and gets the info '''

    html = requests.get(url).text
    bs_obj = BeautifulSoup(html, 'lxml')

    info = {}

    info['name'] = bs_obj.h1.text

    for row in bs_obj.findAll('dd', attrs={'class': 'statsDef-content-list-item'}):
        key = row.find(
            'div', {'class': 'statsDef-content-list-item-label'}).text
        value = row.find(
            'div', {'class': 'statsDef-content-list-item-value'}).text.strip()
        info[key] = value

    return info


if __name__ == "__main__":
    list_of_links = (get_all_links(f'{base_url}/dogs/dog-breeds?page={i}')
                     for i in range(16))

    for links in list_of_links:
        for link in links:
            print(get_info(base_url + link))

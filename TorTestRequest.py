import requests
from bs4 import BeautifulSoup

proxies = {'http': 'socks5h://localhost:9050'}

url = 'https://example.mx/'

source_code = requests.get(url, proxies=proxies)
soup = BeautifulSoup(source_code, 'html.parser')

output = []

# Obtaining urls from raw html page

for link in soup.findAll('a', href=True):
    if re.search('#', link['href']):
        continue
    if re.search(':', link['href']):
        continue
    output.append({'url': urljoin(node['url'], link["href"]), 'depth': node['depth'] + 1})

print(output)

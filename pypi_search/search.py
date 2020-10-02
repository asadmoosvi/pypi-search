from bs4 import BeautifulSoup
from typing import Dict, Optional, List
import requests


def find_packages(query: str) -> Optional[List[Dict[str, str]]]:
    query = '+'.join(query.split())
    response = requests.get(f'http://pypi.org/search/?q={query}')
    if response.status_code != requests.codes.ok:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    package_snippets = soup.find_all('a', class_='package-snippet')
    search_results = list()
    for package_snippet in package_snippets:
        span_elems = package_snippet.find_all('span')
        name = span_elems[0].text.strip()
        version = span_elems[1].text.strip()
        release_date = span_elems[2].text.strip()
        desc = package_snippet.p.text.strip()
        search_results.append(
            dict(
                name=name,
                version=version,
                release_date=release_date,
                description=desc
            )
        )
    return search_results

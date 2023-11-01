import requests
from bs4 import BeautifulSoup
import lxml


person_url_list = []
# 1. only 20 members are expected on the page, access each page with an interview of 20
for i in range(0, 760, 20):
    url = f'https://www.bundestag.de/ajax/filterlist/en/members/863330-863330?limit=12&noFilterSet=true&offset={i}'
    # print(url)

    q = requests.get(url)
    result = q.content

# 2. select all href links of all persons from each page, where href in <a> in <div> class name= bt-slide-content
    soup = BeautifulSoup(result, 'lxml')
    persons = soup.findAll('div', attrs={'class': 'bt-slide-content'})

    for person in persons:
        person_page_url = person.find('a')['href']
        person_url_list.append(person_page_url)

# 3. save href links in a file
with open("person_url_list.txt", 'w') as file:
    for line in person_url_list:
        file.write(f'{line}\n')

# ---   don't access the web page each time,  but save and use the info from a saved file: person_url_list.txt

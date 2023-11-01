import requests
from bs4 import BeautifulSoup
import lxml
import json


data_dict = []
count = 0

q = requests.get('https://www.bundestag.de/en/members/abdi_sanae-861028')
result = q.content

soup = BeautifulSoup(result, 'lxml')
person = soup.find(class_='bt-biografie-name').find('h3').text
person_name_company = person.strip().split(',')
person_name = person_name_company[0]
person_company = person_name_company[1].strip()

div_element = soup.find('div', class_='col-xs-12 col-md-4')

social_networks = div_element.find_all('a')

social_networks_url = []
for item in social_networks:
        social_networks_url.append(item.get('href'))

# 6. create a dic of each person that save name, company and social links
data = {
    'person_name': person_name,
    'person_company': person_company,
    'social_networks': social_networks_url
}
# 7. print the number and link that was done
count += 1
print(f'#{count}: is done')

# 8. save each person info (dic) in a list
data_dict.append(data)

# 9. save all info from list data_dic in a json file
with open('data.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

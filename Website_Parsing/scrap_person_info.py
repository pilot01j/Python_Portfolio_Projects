import requests
from bs4 import BeautifulSoup
import lxml
import json

# 4. access all links from a file and select person name and company using class name and h3
with open('person_url_list.txt') as file:
    lines = [line.strip() for line in file.readlines()]

    data_dic = []
    count = 0

    for line in lines:
        q = requests.get(line)
        result = q.content

        soup = BeautifulSoup(result, 'lxml')
        person = soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company = person.strip().split(',')
        person_name = person_name_company[0]
        person_company = person_name_company[1].strip()


# ------ 5. select from a links all social profile on internet of each person
        div_element = soup.find('div', class_='col-xs-12 col-md-4')
        social_networks = div_element.find_all('a')

        social_networks_url = []
        for item in social_networks:
            social_networks_url.append(item.get('href'))

# ------ 6. create a dic of each person that save name, company and social links
        data = {
            'person_name': person_name,
            'person_company': person_company,
            'social_networks': social_networks_url
        }
# ----- 7. print the number and link that was done
        count += 1
        print(f'#{count}: {line} is done!')

# ----- 8. save each person info(dic) in a list
        data_dic.append(data)

# ----- 9. save all info from list data_dic in a json file
        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data_dic, json_file, indent=4, ensure_ascii=False)




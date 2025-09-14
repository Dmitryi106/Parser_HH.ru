import json

import requests

url_get = "https://api.hh.ru/vacancies"
response = requests.get(url_get)
print(response.status_code)
print(response.text)

vacancy = response.json()
with open("vacancies.json","w",encoding='utf-8') as file_vacancy:
    json.dump(vacancy, file_vacancy, ensure_ascii=False, indent=2)
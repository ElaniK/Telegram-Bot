import requests
import json

base_key = 'RUB'
sym_key = 'USD'
amount = '10'

url = f"https://api.apilayer.com/fixer/convert?to=USD&from=RUB&amount=1"
headers = {"apikey": "2TMuBgqhX0MMIFAUgrjoChLit9QossM2"}

response = requests.request("GET", url, headers=headers)
res = json.loads(response.content)
print(res)

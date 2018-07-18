import json
import requests

asi_key='2306179'
url='https://www.metaweather.com/api/location/'+asi_key
r=requests.get(url)
r.encoding='urf-8'
print(type(r.text))

#show json
data=json.loads(r.text)
data2=json.dumps(data, indent=4)
print(data2)

for i in data['consolidated_weather']:
    print('min_temp : ',i['min_temp'])
    print('predictability',i['predictability'])
    print('weather_state_name',i['weather_state_name'])
    print('-'*50)
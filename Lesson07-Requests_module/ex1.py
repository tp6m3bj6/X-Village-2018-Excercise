#處理獨立音樂展演資料
import requests
import json

#download
url='https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'
response=requests.get(url)

#write  music_show.json
#將上述網址寫入json中
f=open('music_show.json','w+')
f.write(response.text)
f.close()


#open Json
with open('music_show.json') as f:
    SearchShowAction = json.load(f)
    p=json.dumps(SearchShowAction, indent=4)
    print(p)

#取檔案,write2
f2=open('music_show.txt','w')
p2=json.loads(p)
l=len(p2)
for i in range(l):
    f2.write(p2[i]["title"]+':'+p2[i]["startDate"]+"~"+p2[i]["endDate"]+'\n')
f2.close()

#Print 產生的txt檔測試
with open('music_show.txt','r', encoding='utf-8-sig') as f3:
    print(f3.read())

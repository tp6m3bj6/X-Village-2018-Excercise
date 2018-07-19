# ex2.1 的 Sample code
import matplotlib.pyplot as plt
import pandas as pd
url = 'http://markets.financialcontent.com/stocks/action/gethistoricaldata?Month=12&Symbol=GOOG&Range=300&Year=2017'
google_stock = pd.read_csv(url)
new_google_stock = google_stock.iloc[::-1] # 因為收到的資料是從 12/29/17 開始到 03/28/14，因此要轉個方向變成3/28/14到12/29/17。
new_google_stock = new_google_stock[:30] # 為了讓上下間距區域變明顯，我們只看前面30天的資料
# print(new_google_stock)
plt.figure(figsize=(10, 5))
# 
# (rows, cols)
x = range(0,new_google_stock.shape[0]) # [0,1,2...,945] # 產生 x 座標用
y = new_google_stock['Open'] # 取得 Open 那一欄的所有資料，用來當 y 座標。
yl= new_google_stock['High']
yh= new_google_stock['Low']
plt.plot(x, y, color='blue', linewidth=2.0, linestyle=':') 
plt.fill_between(x,yh,yl,color='yellow')
plt.show()
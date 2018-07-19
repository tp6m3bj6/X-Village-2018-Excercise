# sample code
import pandas as pd
table = [
    ['A', 'Noah', 90, 92],
    ['B', 'Liam', 81, 83],
    ['C', 'William', 87,85],
    ['B', 'Benjamin.', 82,80],
    ['A', 'Emma.', 90,94],
    ['C', 'Olivia', 50,60],
    ['A', 'Isabella', 70,71],
    ['C', 'Amelia', 84,86],
    ['B', 'Mia', 88,85],
]
df = pd.DataFrame(table,columns = ['class', 'name', 'math_score', 'eng_score'])
print(df)

# total score數學分數平均值
total_score=df['math_score'].mean()
print(total_score)
# 數學分數總和 - - - (A班平均多少，總分多少，B班平均...)
m=df.groupby('class').mean()
print(m)
# print("A班平均："＋Amean＋"總分 ："＋Atotalscore)
s=df.groupby('class').sum()
print(s)
# 數學分數與英文分數的相關係數
c=df.corr()
print(c)
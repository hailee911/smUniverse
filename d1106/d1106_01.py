# 데이터 분석
import pandas as pd
# 1차원 - series, 2차원 - DataFrame

# series
# 1차원 (정수/실수/문자열 등)
temp = pd.Series([-20,-10,10,20],index=['Jan','Fab','Mar','Apr'])
print(temp)

print(temp['Jan'])
print(temp['Fab'])
print(temp['Mar'])

# ----------------

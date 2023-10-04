from utils import module as md
import pandas as pd
import matplotlib.pyplot as plt

# 기본 데이터 전처리

df_main = pd.read_csv('산업통상자원부_반도체디스플레이 수출동향 추이_20221231.csv')
df = df_main.copy()
df['년월'] = pd.to_datetime(df['년월'])
df.set_index('년월', inplace=True)
df_year = df.resample('Y').sum()
df_year_ = df_year.iloc[:,[0,2,4,6,8,10,12]]
# 그래프

fig = md.sidexport(df_year) # 반도체 수출(각 항목의 비율 표시)
plt.show()


fig = md.exportplot(df_year, '반도체(억불)', '메모리(억불)', '시스템_반도체(억불)', '개별소자(억불)')
plt.show()  # 반도체 + 메모리 + 비 메모리 수출

fig = md.memoryratio(df_year)
plt.show()



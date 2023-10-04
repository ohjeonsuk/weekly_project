import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fontprop = fm.FontProperties(fname='NanumGothic.ttf')


def data():
    df_main = pd.read_csv('산업통상자원부_반도체디스플레이 수출동향 추이_20221231.csv')
    df = df_main.copy()
    df['년월'] = pd.to_datetime(df['년월'])
    df.set_index('년월', inplace=True)
    df_year = df.resample('Y').sum()
    df_year_ = df_year.iloc[:,[0,2,4,6,8,10,12]]
    return df, df_year

def test5(df, *args):
    fig = plt.figure(figsize=(10,5))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(df.index.year, df[list(args)].values, label=list(args))
    ax.legend(prop=fontprop)
    ax.set_title('반도체(메모리+시스템+개별소자) 수출', fontproperties=fontprop, fontsize = 11)
    return plt
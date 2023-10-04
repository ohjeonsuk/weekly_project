import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm

fontprop = fm.FontProperties(fname='NanumGothic.ttf')

def data1():
    df = pd.read_csv('메모리.csv')
    df1 = pd.read_csv('시스템.csv')
    start_date = '2015-01-01'

    # 시계열 인덱스 생성
    date_index = pd.date_range(start=start_date, periods=len(df), freq='M')
    df.set_index(date_index, inplace=True)
    df1.set_index(date_index, inplace=True)
    return df, df1

def test6(df, df1):
    fig, ax = plt.subplots(figsize=(12 ,8))
    ax.plot(df.index, df['합계'], label='메모리')
    ax.plot(df1.index, df1['합계'], label='시스템')

    ax.set_title('메모리 반도체 vs 시스템 반도체 수출액', fontsize = 18)
    ax.set_ylabel('금액' ,fontsize = 14)
    ax.legend()
    return plt

def test7(file_path, list):
    df = pd.read_csv(file_path)
    df = df[list]

    df['년월'] = pd.to_datetime(df['년월'])

    df['년월'] = pd.to_datetime(df['년월'])

    fig, ax = plt.subplots(figsize=(6, 7.5))
    ax.plot(df['년월'], df['메모리_전년동월대비_증감률(퍼센트)'], label='메모리')
    ax.plot(df['년월'], df['시스템_반도체_전년동월대비_증감률(퍼센트)'], label='시스템')
    ax.set_title('메모리 vs 시스템 전년동월대비 증감률', fontsize = 18)
    ax.legend()
    return plt
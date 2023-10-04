import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.font_manager as fm

fontprop = fm.FontProperties(fname='NanumGothic.ttf')

def data2():
    df = pd.read_excel('수출액 증감률.xlsx')
    df['월'] = df['분기'].str.extract('(\d+)분기').astype(int)
    quarter_to_month = {1: 3, 2: 6, 3: 9, 4: 12}
    df['월'] = df['월'].map(quarter_to_month)
    df['연도'] = df['분기'].str.extract('(\d+)년').astype(int)
    df['날짜'] = pd.to_datetime(df['연도'].astype(str) + '-' + df['월'].astype(str) + '-01', format='%Y-%m-%d')
    df = df[['날짜', '증감률']]

    df4 = pd.read_excel('GDP.xlsx', skiprows=[0])
    df4.columns = ['Date', '명목GDP', '실질GDP성장률']
    df4 = df4.drop(0)
    df4 = df4.iloc[13:33]
    df4['Year'] = df4['Date'].str.extract('(\d{4})').astype(int)
    df4['Quarter'] = df4['Date'].str.extract('(\d)(?=/4)').astype(int)
    df4['Month'] = df4['Quarter'].map({1: 3, 2: 6, 3: 9, 4: 12})
    df4['Date'] = pd.to_datetime(df4['Year'].astype(str) + df4['Month'].astype(str).str.zfill(2) + '01', format='%Y%m%d')
    return df, df4

def test7(df, df4):
    font_path = "NanumGothic.ttf" 
    fontprop = fm.FontProperties(fname=font_path)
    sns.set(style="whitegrid")
    fig, ax1 = plt.subplots(figsize=(12, 6))

    # 첫 번째 그래프 (증감률)
    ax1.set_ylabel('증감률', color='tab:blue',fontproperties=fontprop)
    ax1.plot(df['날짜'], df['증감률'], color='tab:blue', marker='o', linestyle='-')
    ax1.tick_params(axis='y', labelcolor='tab:blue')

    # 두 번째 그래프 (실질GDP 성장률)
    ax2 = ax1.twinx()  # 두 번째 y축을 사용
    ax2.set_ylabel('실질GDP 성장률', color='tab:red',fontproperties=fontprop)
    ax2.plot(df4['Date'], df4['실질GDP성장률'], color='tab:red', marker='o', linestyle='-')
    ax2.tick_params(axis='y', labelcolor='tab:red')

    plt.title('실질 GDP 성장률과 국내 수출액 증감률 비교',fontproperties=fontprop, fontsize = 19)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.legend()
    return plt

def test8(df2):
    df2 = pd.read_excel('가공단계별수출.xlsx')
    df2['년도'] = df2['년도'].str.extract('(\d+)').astype(int)
    total = df2[['1차 산품', '소비재', '자본재', '중간재', '기타']].sum(axis=1)
    for col in ['1차 산품', '소비재', '자본재', '중간재', '기타']:
        df2[col] = (df2[col] / total) * 100  # 비중 계산 및 백분율로 변환
    sns.set(style='whitegrid')
    colors = sns.color_palette("husl", 5)
    plt.figure(figsize=(10, 5))
    plt.rcParams['font.family'] = 'NanumGothic'
    plt.bar(df2['년도'], df2['1차 산품'], label='1차 산품',  width=0.2, color = colors[0])
    plt.bar(df2['년도'] + 0.2, df2['소비재'], label='소비재',  width=0.2, color = colors[1])
    plt.bar(df2['년도'] + 0.4, df2['자본재'], label='자본재',   width=0.2, color = colors[2])
    plt.bar(df2['년도'] + 0.6, df2['중간재'], label='중간재',   width=0.2, color = colors[3])
    plt.bar(df2['년도'] + 0.8, df2['기타'], label='기타', width=0.2, color = colors[4])

    plt.title('년도별 단계별 비중 막대그래프', fontproperties=fontprop, fontsize = 18)
    plt.ylabel('비중 (%)')
    plt.xticks(df2['년도'])
    plt.legend()
    plt.tight_layout()
    return plt

def test9():
    df3 = pd.read_excel('가공단계별증감률.xlsx')
    df3.set_index('년도', inplace=True)
    sns.set(style='whitegrid')
    plt.figure(figsize=(12, 8))
    plt.rcParams['font.family'] = 'NanumGothic'
    for col in df3.columns:
        plt.plot(df3.index, df3[col], label=col, marker = 'o', linewidth=3)

    plt.title('년도별 단계별 수출액 증감률', fontproperties=fontprop, fontsize = 30)
    plt.ylabel('증감률 (%)')
    plt.legend(fontsize=25)
    plt.grid(True)
    plt.tight_layout()
    return plt
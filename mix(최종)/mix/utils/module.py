# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 14:19:46 2023

@author: rnjsd
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
from scipy import stats
import matplotlib.dates as mdates


font_path = 'NanumGothic.ttf'
fontprop = fm.FontProperties(fname=font_path)
plt.rc('font', family='NanumGothic')

def diff(df, column):
    result_df = df[column].diff().abs()
    return result_df

def diffError(df, column):
    df_diff = diff(df, column)
    for date in df_diff.index:
        if df_diff.loc[date] > 3:
            df.loc[date, column] = np.nan
    return df

def diffSumError(df,column):
    df_diff = diff(df, column)
    error = df_diff.resample('H').sum()[df_diff.resample('H').sum() < 0.1]
    for i in range(len(error)):
        df.loc[str(error.index[i])[:-6]].loc[:, column] = np.nan
    return df

def toNan(df):
    df.fillna(np.nan, inplace=True)
    return df

def groupDay(df, new_column):
    df_copy = df.copy()
    df_copy[new_column] = pd.cut(df_copy.index.hour,
       bins = [0, 4, 8, 16, 20, 23],
       labels = ['새벽', '아침', '낮', '저녁', '밤'],
       include_lowest=True)
    return df_copy

#밤낮 평균, 최대, 최소 온도
def monthstemp(df_day): 
    df_day_gpd = df_day['기온(섭씨)'].groupby(df_day['day']).agg(['mean', 'max', 'min'])
    return df_day_gpd


# 8월1일~8월20일간의 하루 평균 기온
def hourmeantemp(df_itp):
    df_itp['시간'] = df_itp.index.hour
    df_hour_mean = pd.DataFrame(df_itp['기온(섭씨)'].groupby(df_itp['시간']).mean())
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(df_hour_mean.index, df_hour_mean['기온(섭씨)'])
    ax.set_title('하루 평균 기온',fontproperties=fontprop, fontsize=15)
    ax.set_xticks(df_hour_mean.index)
    ax.set_xlabel('시간', fontproperties=fontprop, fontsize=13)
    ax.set_ylabel('기온', fontproperties=fontprop, fontsize=13, rotation=0)
    return fig

def checkData(df):
    df_copy = df.copy()
    mask = df_copy['기온(섭씨)'].resample('H').count() < 60*0.8
    df_count = df_copy.resample('H').count()[mask]
    if df_count.empty:
        pass
    else:
        df_copy.loc[:,:'일조(Sec)'] = df_copy.loc[:,:'일조(Sec)'].interpolate(method='time')
    return df_copy

def printcheckData(df):
    df_copy = df.copy()
    mask = df_copy['기온(섭씨)'].resample('H').count() < 60*0.8
    df_count = df_copy.resample('H').count()[mask]
    return df_count

def makedaydf(df):	# 일별 절기에 해당하는 평균 기온
    day_list = ['새벽', '아침', '낮', '저녁', '밤']
    for day in day_list:
        mask = df['day'] == day
        if day == '새벽':
            df_dawn = df.loc[:,:'일조(Sec)'][mask].resample('D').mean()
        elif day == '아침':
            df_morning = df.loc[:,:'일조(Sec)'][mask].resample('D').mean()
        elif day == '낮':
            df_daytime = df.loc[:,:'일조(Sec)'][mask].resample('D').mean()
        elif day == '저녁':
            df_evening = df.loc[:,:'일조(Sec)'][mask].resample('D').mean()
        else:
            df_night = df.loc[:,:'일조(Sec)'][mask].resample('D').mean()
    return df_dawn, df_morning, df_daytime, df_evening, df_night

# 8월1일 ~ 8월 20일 기온
def hourgraph(df_original, df_itp):				# 시간별 기온, 강수량, 풍속 그래프
    df_original_hour_gpd = df_original.resample('H').agg(['mean', 'max', 'min'])
    df_itp_hour_gpd = df_itp.resample('H').agg(['mean', 'max', 'min'])
    fig = plt.figure(figsize=(10,8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(df_original_hour_gpd.index, df_original_hour_gpd['기온(섭씨)']['mean'], label='기온(섭씨)')
    ax1.plot(df_original_hour_gpd.index, df_original_hour_gpd['누적강수량(mm)']['mean'], label='누적 강수량(mm))')
    ax1.plot(df_original_hour_gpd.index, df_original_hour_gpd['풍속(m/s)']['mean'], label='풍속(m/s)')
    ax1.legend(loc='best', prop=fontprop)
    ax1.set_title('시간별 기온', fontproperties=fontprop) 

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['기온(섭씨)']['mean'], label='기온(섭씨)')
    ax2.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['누적강수량(mm)']['mean'], label='누적 강수량(mm))')
    ax2.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['풍속(m/s)']['mean'], label='풍속(m/s)')
    ax2.legend(loc='best', prop=fontprop)
    ax2.set_title('시간별 기온 - 보간', fontproperties=fontprop)

    return fig

def dailygraph(df_original, df_itp):				# 일일 기온, 강수량, 풍속 그래프
    df_original_day_gpd = df_original.resample('D').agg(['mean', 'max', 'min'])
    df_itp_day_gpd = df_itp.resample('D').agg(['mean', 'max', 'min'])
    fig = plt.figure(figsize=(10,8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(df_original_day_gpd.index, df_original_day_gpd['기온(섭씨)']['mean'], label='기온(섭씨)')
    ax1.plot(df_original_day_gpd.index, df_original_day_gpd['누적강수량(mm)']['mean'], label='누적 강수량(mm))')
    ax1.plot(df_original_day_gpd.index, df_original_day_gpd['풍속(m/s)']['mean'], label='풍속(m/s)')
    ax1.legend(loc='best', prop=fontprop)
    ax1.set_title('일별 기온', fontproperties=fontprop) 
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(df_itp_day_gpd.index, df_itp_day_gpd['기온(섭씨)']['mean'], label='기온(섭씨)')
    ax2.plot(df_itp_day_gpd.index, df_itp_day_gpd['누적강수량(mm)']['mean'], label='누적 강수량(mm))')
    ax2.plot(df_itp_day_gpd.index, df_itp_day_gpd['풍속(m/s)']['mean'], label='풍속(m/s)')
    ax2.legend(loc='best', prop=fontprop)
    ax2.set_title('일별 기온 - 보간', fontproperties=fontprop)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)   
    fig.subplots_adjust(hspace=0.5)
    return fig

# 이동 평균 그래프 : 1시간, 3시간, 8시간, 1일
def meangraph(df_itp):
    df_itp_copy = df_itp.copy()
    df_1H = df_itp_copy['기온(섭씨)'].rolling('H').mean()
    df_1H_gpd = df_1H.resample('D').mean()
    df_3H = df_itp_copy['기온(섭씨)'].rolling('3H').mean()
    df_3H_gpd = df_3H.resample('D').mean()
    df_8H = df_itp_copy['기온(섭씨)'].rolling('8H').mean()
    df_8H_gpd = df_8H.resample('D').mean()
    df_1DAY = df_itp_copy['기온(섭씨)'].rolling('D').mean()
    df_1DAY_gpd = df_1DAY.resample('D').mean()
    df_gpd = df_itp_copy['기온(섭씨)'].resample('D').mean()
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(1, 1, 1)
    #ax.plot(df_1H_gpd.index, df_1H_gpd.values, linestyle='--', label = '1시간')
    #ax.plot(df_3H_gpd.index, df_3H_gpd.values, linestyle='--', label = '3시간')
    #ax.plot(df_8H_gpd.index, df_8H_gpd.values, linestyle='--', label = '8시간')
    #ax.plot(df_1DAY_gpd.index, df_1DAY_gpd.values, linestyle='--', label = '1일')
    #ax.plot(df_gpd.index, df_gpd.values, label ='원본')
    ax.plot(df_1H.index, df_1H.values, linestyle='--', label = '1시간')
    ax.plot(df_3H.index, df_3H.values, linestyle='--', label = '3시간')
    ax.plot(df_8H.index, df_8H.values, linestyle='--', label = '8시간')
    ax.plot(df_1DAY.index, df_1DAY.values, linestyle='--', label = '1일')
    ax.plot(df_itp_copy.index, df_itp_copy['기온(섭씨)'], label = '원본')
    ax.legend(prop=fontprop)
    ax.set_title('이동 평균 기온', fontproperties=fontprop, fontsize=15)
    ax.set_xticks(df_1DAY_gpd.index)
    ax.set_xticklabels(df_1DAY_gpd.index.strftime('%Y-%m-%d'), rotation=90)
    ax.set_ylabel('기온', fontproperties=fontprop, rotation=0, fontsize=13)
    ax.grid(True)
    return fig

# 월간 일일 낮, 아침 온도 비교 (이유:평균 온도가 아침이 제일 낮고, 낮이 제일 높아서)
def dailytemp(df_day):
    df_dawn, df_morning, df_daytime, df_evening, df_night = makedaydf(df_day)
    fig = plt.figure(figsize = (10,8))
    ax1 = fig.add_subplot(2, 1, 1)
    ax1.plot(df_dawn.index, df_dawn['기온(섭씨)'], label='새벽')
    ax1.plot(df_morning.index, df_morning['기온(섭씨)'], label='아침')
    ax1.plot(df_daytime.index, df_daytime['기온(섭씨)'], label='낮')
    ax1.plot(df_evening.index, df_evening['기온(섭씨)'], label='저녁')
    ax1.plot(df_night.index, df_night['기온(섭씨)'], label='밤')
    ax1.legend(loc='lower left', prop=fontprop)
    ax1.set_title('시간대 평균 기온', fontproperties=fontprop, fontsize=15)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=90)

    ax2 = fig.add_subplot(2, 1, 2)
    ax2.plot(df_morning.index, df_morning['기온(섭씨)'], color='orange', label='아침')
    ax2.plot(df_daytime.index, df_daytime['기온(섭씨)'], color='green', label='낮')
    ax2.legend(prop=fontprop)
    ax2.set_title('낮-아침 평균 기온', fontproperties=fontprop, fontsize=15)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)
    fig.subplots_adjust(hspace=0.5)
    
    max_daytime = df_daytime['기온(섭씨)'].max()
    min_daytime = df_daytime['기온(섭씨)'].min()
    max_morning = df_morning['기온(섭씨)'].max()
    min_morning = df_morning['기온(섭씨)'].min()
    ax2.plot(df_morning['기온(섭씨)'].idxmax(), max_morning, 'bo')
    ax2.annotate(f'{max_morning:.2f}', xy=(df_morning['기온(섭씨)'].idxmax(), max_morning), fontsize=10, xytext=(0, -50),
             textcoords='offset points', arrowprops=dict(arrowstyle='->', color='blue'))
    ax2.plot(df_morning['기온(섭씨)'].idxmin(), min_morning, 'bo')
    ax2.annotate(f'{min_morning:.2f}', xy=(df_morning['기온(섭씨)'].idxmin(), min_morning), fontsize=10, xytext=(0, 60),
             textcoords='offset points', arrowprops=dict(arrowstyle='->', color='blue'))
    
    ax2.plot(df_daytime['기온(섭씨)'].idxmax(), max_daytime, 'ro')
    ax2.annotate(f'{max_daytime:.2f}', xy=(df_daytime['기온(섭씨)'].idxmax(), max_daytime), fontsize=10, xytext=(50, -10),
             textcoords='offset points', arrowprops=dict(arrowstyle='->', color='red'))
    ax2.plot(df_daytime['기온(섭씨)'].idxmin(), min_daytime, 'ro')
    ax2.annotate(f'{min_daytime:.2f}', xy=(df_daytime['기온(섭씨)'].idxmin(), min_daytime), fontsize=10, xytext=(-50, 0),
             textcoords='offset points', arrowprops=dict(arrowstyle='->', color='red'))
    return fig

#산점도를 통해 선형성 파악
def scatt(df):
    df_copy = df.copy()
    fig = plt.figure(figsize=(10,8))
    ax1 = fig.add_subplot(2,5,1)
    ax2 = fig.add_subplot(2,5,2)
    ax3 = fig.add_subplot(2,5,3)
    ax4 = fig.add_subplot(2,5,4)
    ax5 = fig.add_subplot(2,5,5)
    ax6 = fig.add_subplot(2,5,6)
    ax7 = fig.add_subplot(2,5,7)
    ax8 = fig.add_subplot(2,5,8)
    ax9 = fig.add_subplot(2,5,9)
    ax10 = fig.add_subplot(2,5,10)
    ax_list=[ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10]

    plt.subplots_adjust(wspace=0.6)

    for i, column in enumerate(df_copy.columns[1:]):
        ax_list[i].scatter(df_copy[column], df_copy['기온(섭씨)'], s=0.1)
        ax_list[i].set_xlabel(f'{column}')
        ax_list[i].set_ylabel('기온(섭씨)')
            
    return fig

#상관관계
def corr(df):
    df_copy = df.copy()
    alpha = 0.05
    p_values_df = pd.DataFrame(index=df_copy.columns, columns=df_copy.columns)
    for column1 in df_copy.columns:
        for column2 in df_copy.columns:
            if column1 != column2:
                result = stats.pearsonr(df_copy[column1], df_copy[column2])
                p_value = result[1]
                p_values_df.loc[column1, column2] = p_value
    return p_values_df
    
#기온과 상관관계에 있는 변수들
def hourgraph_all(df_itp):				# 시간별 기온, 강수량, 풍속 그래프
    df_itp_hour_gpd = df_itp.resample('H').agg(['mean', 'max', 'min'])
    fig = plt.figure(figsize=(10,8))
    ax1 = fig.add_subplot(1, 1, 1)
    ax1.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['기온(섭씨)']['mean'], label='기온(섭씨)')
    ax1.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['누적강수량(mm)']['mean'], label='누적 강수량(mm))')
    ax1.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['습도(%)']['mean'], label='습도(%)')
    ax1.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['일사(MJ/m^2)']['mean'], label='일사(MJ/m^2)')
    ax1.set_title('시간별 기온', fontproperties=fontprop, size=20)
    # 시간 레이블 포맷팅
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=1))  # 일 간격으로 눈금 설정
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=90)
    ax1.set_xlim(pd.to_datetime('2023-08-01 00:00:00'), pd.to_datetime('2023-08-20 23:00:00'))

    ax2 = ax1.twinx()
    ax2.plot(df_itp_hour_gpd.index, df_itp_hour_gpd['일조(Sec)']['mean'], color='black', label='일조(Sec)')
    ax1.grid(True)
    ax2.grid(True)
    fig.legend(loc='upper right', prop=fontprop)
    
    return fig

# 그래프에서 하루씩만 추출
def hourgraph_oneday(df_itp):
    df_itp_hour_first = df_itp['2023-08-02'].resample('H').agg(['mean', 'max', 'min'])
    df_itp_hour_tenth = df_itp['2023-08-10'].resample('H').agg(['mean', 'max', 'min'])
    fig = plt.figure(figsize=(10,8))
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.plot(df_itp_hour_first.index, df_itp_hour_first['기온(섭씨)']['mean'], label='기온(섭씨)')
    ax1.plot(df_itp_hour_first.index, df_itp_hour_first['누적강수량(mm)']['mean'], label='누적 강수량(mm))')
    ax1.plot(df_itp_hour_first.index, df_itp_hour_first['습도(%)']['mean'], label='습도(%)')
    ax1.plot(df_itp_hour_first.index, df_itp_hour_first['일사(MJ/m^2)']['mean'], label='일사(MJ/m^2)')
    ax1.set_title('8월 2일', fontproperties=fontprop, size=20)
    ax1.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # 일 간격으로 눈금 설정
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    ax1.set_xlim(pd.to_datetime('2023-08-02 00:00:00'), pd.to_datetime('2023-08-02 23:00:00'))
    ax1.set_xlabel('시간', fontproperties=fontprop)
    plt.xticks(rotation=45)
    ax2 = ax1.twinx()
    ax1.grid(True)
    ax2.plot(df_itp_hour_first.index, df_itp_hour_first['일조(Sec)']['mean'], color='black', label='일조(Sec)')

    ax3 = fig.add_subplot(1, 2, 2)
    ax3.plot(df_itp_hour_tenth.index, df_itp_hour_tenth['기온(섭씨)']['mean'])
    ax3.plot(df_itp_hour_tenth.index, df_itp_hour_tenth['누적강수량(mm)']['mean'])
    ax3.plot(df_itp_hour_tenth.index, df_itp_hour_tenth['습도(%)']['mean'])
    ax3.plot(df_itp_hour_tenth.index, df_itp_hour_tenth['일사(MJ/m^2)']['mean'])
    ax3.set_title('8월 10일', fontproperties=fontprop, size=20)
    ax3.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # 일 간격으로 눈금 설정
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%H'))
    ax3.set_xlim(pd.to_datetime('2023-08-10 00:00:00'), pd.to_datetime('2023-08-10 23:00:00'))
    ax3.set_xlabel('시간', fontproperties=fontprop)
    plt.xticks(rotation=45)
    ax4 = ax3.twinx()
    ax3.grid(True)
    ax4.plot(df_itp_hour_tenth.index, df_itp_hour_tenth['일조(Sec)']['mean'], color='black')
    fig.legend(loc='upper right', prop=fontprop)
    return fig

def sidexport(df):
    n_df = df.copy()
    year_list = n_df.index.year.tolist()
    sid_dict = {}
    for column in n_df.loc[:,['메모리(억불)', '시스템_반도체(억불)', '개별소자(억불)']].columns:
        sid_dict[column] = n_df[column].values
        
    width = 0.5  # the width of the bars: can also be len(x) sequence


    fig, ax = plt.subplots()
    bottom = np.zeros(len(sid_dict['메모리(억불)']))

    for key, value in sid_dict.items():
        p = ax.bar(year_list, value, width, label=key[:-4], bottom=bottom)
        bottom += value

        ax.bar_label(p, label_type='center')

    ax.set_title('반도체 수출', fontproperties=fontprop, fontsize=15)
    ax.legend(prop=fontprop)
    ax.set_ylabel('억불', fontproperties=fontprop, rotation=0)
    return fig
    
def exportplot(df, *args):
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(df.index.year, df[list(args)].values, label=list(args))
    ax.legend(prop=fontprop)
    ax.set_title('반도체(메모리+시스템+개별소자) 수출', fontproperties=fontprop, fontsize = 15)
    return fig


def memoryratio(df):
    n_df = df.copy()
    n_df['메모리_D램 비율'] = n_df['메모리_D램(억불)'] / n_df['메모리(억불)'] * 100
    n_df['메모리_낸드 비율'] = n_df['메모리_낸드(억불)'] / n_df['메모리(억불)'] * 100
    n_df['메모리_MCP 비율'] = n_df['메모리_MCP(억불)'] / n_df['메모리(억불)'] * 100
    n_df['기타'] = 100 - n_df['메모리_D램 비율'] - n_df['메모리_낸드 비율'] - n_df['메모리_MCP 비율']
    columns_list = list(n_df.columns[-4:])
    export_dict = {}
    for year in n_df.index.year:
        export_dict[year]= n_df.loc[str(year)].loc[:, columns_list].values[0].tolist()
    
    labels = list(export_dict.keys())
    data = np.array(list(export_dict.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](
        np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(9.2, 5))
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max())

    for i, (colname, color) in enumerate(zip(columns_list, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname.split(' ')[0], color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        ax.bar_label(rects, label_type='center', color=text_color)
    ax.legend(ncols=len(columns_list), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize='small', prop=fontprop)
    return fig

    
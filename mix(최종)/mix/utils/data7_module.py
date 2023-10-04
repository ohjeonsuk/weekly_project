import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.font_manager as fm


fontprop = fm.FontProperties(fname='NanumGothic.ttf')

#국가별 반도체 막대그래프
def survey(results, category_names):
    labels = list(results.keys())
    data = np.array(list(results.values()))
    data_cum = data.cumsum(axis=1)
    category_colors = plt.colormaps['RdYlGn'](np.linspace(0.15, 0.85, data.shape[1]))

    fig, ax = plt.subplots(figsize=(12, 8))  # x축 길이를 조정
    ax.invert_yaxis()
    ax.xaxis.set_visible(False)
    ax.set_xlim(0, np.sum(data, axis=1).max() * 1.1)  # x축 범위를 늘림

    for i, (colname, color) in enumerate(zip(category_names, category_colors)):
        widths = data[:, i]
        starts = data_cum[:, i] - widths
        rects = ax.barh(labels, widths, left=starts, height=0.5,
                        label=colname, color=color)

        r, g, b, _ = color
        text_color = 'white' if r * g * b < 0.5 else 'darkgrey'
        # ax.bar_label(rects, label_type='center', color=text_color) 
    ax.legend(ncols=len(category_names), bbox_to_anchor=(0, 1),
              loc='lower left', fontsize=12)

    return fig, ax

def data():
    df = pd.read_csv('국가별 반도체(1).csv')
    country_list = ['China, Hong Kong SAR', 'Other Asia, nes', 'USA', 'Rep. of Korea', 'Singapore', 'China']
    df = df[df['Reporter'].isin(country_list)]
    df['Trade Value (US$)'] = df['Trade Value (US$)'].astype(float)
    df['Year'] = pd.to_datetime(df['Year'], format='%Y')
    grouped = df.groupby(['Year', 'Reporter'])['Trade Value (US$)'].sum().reset_index()
    return grouped

def plot_data(grouped):
    font_path = "NanumGothic.ttf" 
    fontprop = fm.FontProperties(fname=font_path)
    sns.set(style="whitegrid")
    fig, ax = plt.subplots(figsize=(10, 6))

    for country in grouped['Reporter'].unique():
        data = grouped[grouped['Reporter'] == country]
        ax.plot(data['Year'], data['Trade Value (US$)'], label=country, marker='o', linestyle='-')

    plt.xlabel('Year')
    plt.ylabel('수출액 총합 (US$)', fontproperties=fontprop)
    plt.title('년도별 국가별 반도체 수출액($) 추이', fontproperties=fontprop)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)

    return plt


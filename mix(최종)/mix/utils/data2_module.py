import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import ConnectionPatch
import matplotlib.font_manager as fm

fontprop = fm.FontProperties(fname='NanumGothic.ttf')

def test3(overall_ratios,labels,age_ration,age_labels):
    plt.rcParams['font.family'] = 'NanumGothic'
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 9))
    fig.subplots_adjust(wspace=0)
    tableau_10 = [
    (31, 119, 180), (214, 39, 40)
    , (255, 127, 14), (152, 223, 138), (255, 152, 150),
    (148, 103, 189), (44, 160, 44), (197, 176, 213), (255, 187, 120),(174, 199, 232)
]

    # RGB 값 [0, 1] 범위로 조정
    for i in range(len(tableau_10)):
        r, g, b = tableau_10[i]
        tableau_10[i] = (r / 255.0, g / 255.0, b / 255.0)

    explode = [0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # rotate so that first wedge is split by the x-axis
    angle = -180 * overall_ratios[0]
    wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=angle,
                     labels=labels, colors=tableau_10, explode=explode, textprops={'fontsize': 9})

    # bar chart parameters
    bottom = 1
    width = .2

    # Adding from the top matches the legend.
    for j, (height, label) in enumerate(reversed([*zip(age_ration, age_labels)])):
        bottom -= height
        bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
        ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')

    plt.rcParams['font.family'] = 'NanumGothic'
    ax2.set_title('2022년 반도체 수출 비중')
    ax2.legend()
    ax2.axis('off')
    ax2.set_xlim(- 2.5 * width, 2.5 * width)

    # use ConnectionPatch to draw lines between the two plots
    theta1, theta2 = wedges[0].theta1, wedges[0].theta2
    center, r = wedges[0].center, wedges[0].r
    bar_height = sum(age_ration)

    # draw top connecting line
    x = r * np.cos(np.pi / 180 * theta2) + center[0]
    y = r * np.sin(np.pi / 180 * theta2) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, bar_height), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    con.set_linewidth(2)
    ax2.add_artist(con)

    # draw bottom connecting line
    x = r * np.cos(np.pi / 180 * theta1) + center[0]
    y = r * np.sin(np.pi / 180 * theta1) + center[1]
    con = ConnectionPatch(xyA=(-width / 2, 0), coordsA=ax2.transData,
                      xyB=(x, y), coordsB=ax1.transData)
    con.set_color([0, 0, 0])
    ax2.add_artist(con)
    con.set_linewidth(2)
    return plt


def test4(file_path):
    df_main = pd.read_csv(file_path)
    df = df_main.copy()
    df['년월'] = pd.to_datetime(df['년월'])
    df.set_index('년월', inplace=True)
    df_year = df.resample('Y').sum()
    df_year_ = df_year[['메모리(억불)', '시스템_반도체(억불)', '개별소자(억불)']]

    # 그래프 설정
    fig, ax = plt.subplots(figsize=(10, 5))

    # 기본 색상 설정
    base_color = 'C0'  # 기본 색상

    # 그라데이션 색상 설정
    gradient_colors = [base_color, base_color, base_color]  # 모든 항목에 기본 색상 적용
    alpha_values = [0.1, 0.35, 0.6]  # 각 항목에 대한 alpha 값

    for i in range(3):  # 3개 항목에 대해서만 반복
        # 그라데이션 색상 적용
        color_idx = i % 3
        color = gradient_colors[color_idx]
        alpha = alpha_values[color_idx]

        bars = ax.bar(df_year_.index.year, df_year_.iloc[:, i], label=df_year_.columns[i], color=color, alpha=alpha)

        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.0f}', xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3), textcoords='offset points',
                    ha='center', fontsize=10)
    ax.set_title('연도별 반도체 수출 추이', fontproperties = fontprop)

    # 범례 표시
    plt.rcParams['font.family'] = 'NanumGothic'
    ax.legend(loc='upper left')
    return plt
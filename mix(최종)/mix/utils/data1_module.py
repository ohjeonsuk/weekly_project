import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

fontprop = fm.FontProperties(fname='NanumGothic.ttf')

def test1(file_path, country_list):
    #전처리
    df = pd.read_csv(file_path)
    df['Trade Value (US$)'] = pd.to_numeric(df['Trade Value (US$)'].str.replace('[\$,]', '', regex=True), errors='coerce')
    df = df[df['Reporter'].isin(country_list)]
    df = df.groupby(['Period', 'Reporter'])['Trade Value (US$)'].sum().unstack().fillna(0)
    df = df.pct_change() * 100
    return df

def test2(df):
    file_path = ('국가별 반도체 수출.csv')
    plt.figure(figsize=(16, 5))  
    sns.set(style="darkgrid")

# 첫 번째 서브플롯
    plt.subplot(1, 2, 1)
    plt.rcParams['font.family'] = 'NanumGothic'  
    plt.plot(df.index, df['Rep. of Korea'], color='blue', alpha = 0.5)
    plt.plot(df.index, df['China, Hong Kong SAR'], color='blue', alpha = 0.5)
    plt.fill_between(df.index, df['China, Hong Kong SAR'], df['Rep. of Korea'], color='blue', alpha=0.5)
    plt.ylabel('Export Growth Rate (%)')
    plt.title('한국과 홍콩의 수출 증감율 비교', fontproperties = fontprop)
    plt.grid(True)
    plt.ylim(-35, 80)  

    # 두 번째 서브플롯
    plt.subplot(1, 2, 2)  
    plt.plot(df.index, df['China, Hong Kong SAR'], color='red', alpha = 0.5)
    plt.plot(df.index, df['Singapore'], color='red', alpha = 0.5)
    plt.fill_between(df.index, df['China, Hong Kong SAR'],df['Singapore'], color='red', alpha=0.5)
    plt.title('싱가포르와 홍콩의 수출 증감율 비교', fontproperties = fontprop)
    plt.ylim(-35, 80)  # Y-축 범위 설정
    plt.grid(True)

    plt.tight_layout()
    return plt
    
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

fontprop = fm.FontProperties(fname='NanumGothic.ttf')

def test10():
    df = pd.read_excel('수요별.xlsx')
    df['년도'] = pd.to_datetime(df['년도'])

    # 날짜 열을 인덱스로 설정
    df.set_index('년도', inplace=True)

    # 그래프 스타일 설정
    sns.set(style="whitegrid")

    # 그래프 그리기
    plt.rcParams['font.family'] = 'NanumGothic' 
    fig, ax1 = plt.subplots(figsize=(10, 5)) 

    # 모바일 그래프 그리기 (왼쪽 y 축)
    ax1.plot(df.index, df['모바일'], label='모바일', linestyle='-', linewidth=2, color = 'blue', alpha = 0.5)
    ax1.set_ylabel('모바일', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')

    # 서버 그래프 그리기 (오른쪽 y 축)
    ax2 = ax1.twinx()  # 두 번째 y 축 생성
    ax2.plot(df.index, df['서버'], label='서버', linestyle='-', linewidth=2, color = 'green', alpha = 0.7)
    ax2.set_ylabel('서버', color='green')
    ax2.tick_params(axis='y', labelcolor='green')

    fig.tight_layout()
    plt.title('메모리 반도체 수요 분야(모바일 vs 서버)', fontsize = 15)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    plt.grid(True)
    return plt

def test11():
    df = pd.read_excel('스마트폰출하량.xlsx')
    df['날짜'] = pd.to_datetime(df['날짜'])
    df.set_index('날짜', inplace=True)

    # 그래프 그리기
    plt.figure(figsize=(10, 5))

    # Apple 그래프 그리기
    plt.plot(df.index, df['Apple'], label='Apple', linestyle='-')

    # 특정 날짜에 동그라미 표시
    apple_highlight_dates = ['2018-12-01', '2019-12-01', '2020-12-01', '2021-12-01', '2022-12-01']
    apple_highlight_values = df.loc[apple_highlight_dates]['Apple']
    plt.scatter(apple_highlight_dates, apple_highlight_values,  marker='o', s = 100, label='Highlight (Apple)')

    # Samsung 그래프 그리기
    plt.plot(df.index, df['Samsung'], label='Samsung', linestyle='-')

    # 특정 날짜에 동그라미 표시
    samsung_highlight_dates = ['2019-09-01', '2020-09-01', '2021-03-01', '2022-03-01']
    samsung_highlight_values = df.loc[samsung_highlight_dates]['Samsung']
    plt.scatter(samsung_highlight_dates, samsung_highlight_values,  marker='o', s = 100, label='Highlight (Samsung)')

    plt.ylabel('출하량')
    plt.title('스마트폰 출하량', fontsize = 15)
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.tight_layout()
    return plt

def test12():
    df = pd.read_excel('서버모바일D램생산량.xlsx')
    sns.set(style="whitegrid")

    # 그래프 그리기
    plt.figure(figsize=(10, 5))
    plt.rcParams['font.family'] = 'NanumGothic'  
    # 년도별 서버용 D램
    plt.bar(df['년도'], df['서버용_D램'], label='서버용 D램', width=0.4, color='skyblue', alpha=0.7)  # 색상 및 투명도 설정

    # 년도별 모바일용 D램
    plt.bar(df['년도'] + 0.4, df['모바일용_D램'], label='모바일용 D램', width=0.4, color='orange', alpha=0.7)

    plt.ylabel('생산량(%)')
    plt.title('서버용 D램과 모바일용 D램 생산량 추이', fontsize = 15)
    plt.xticks(df['년도'] + 0.2, df['년도'])  # x 축 레이블 설정
    plt.legend()
    plt.grid(axis='y')

    # 그래프 위에 값을 표시
    for i, val in enumerate(df['서버용_D램']):
        plt.text(df['년도'][i], val + 0.5, str(val), ha='center', va='bottom')
    for i, val in enumerate(df['모바일용_D램']):
        plt.text(df['년도'][i] + 0.4, val + 0.5, str(val), ha='center', va='bottom')
    plt.ylim(0, 50)
    plt.tight_layout()
    return plt


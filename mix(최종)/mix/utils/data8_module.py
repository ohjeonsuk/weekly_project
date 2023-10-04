import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import matplotlib.dates as mdates
import matplotlib.font_manager as fm


fontprop = fm.FontProperties(fname='NanumGothic.ttf')

def load_data():
    # 데이터 불러오고 전처리
    memory_df = pd.read_excel('메모리 수출입.xls', header=3)
    memory_df = memory_df.rename(columns={'년월': '년도'})
    memory_df['년도'] = pd.to_datetime(memory_df['년도'].str.replace('년', '') + '-01-01')  # '년도' 열을 날짜 형식으로 변환

    system_df = pd.read_excel('시스템 수출입.xls', header=3)
    system_df = system_df.rename(columns={'년월': '년도'})
    system_df['년도'] = pd.to_datetime(system_df['년도'].str.replace('년', '') + '-01-01')  # '년도' 열을 날짜 형식으로 변환

    start_date = '2016-01-01'
    end_date = '2023-12-31'
    memory_df = memory_df[(memory_df['년도'] >= start_date) & (memory_df['년도'] <= end_date)]
    system_df = system_df[(system_df['년도'] >= start_date) & (system_df['년도'] <= end_date)]

    
    #종목코드 얻어내기
    code_all=pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download')
    code_df = code_all[0]
    names_samsung = '삼성전자'
    names_sk = 'SK하이닉스'

    expr_str_samsung = f"회사명=='{names_samsung}'"
    code_samsung = code_df.query(expr_str_samsung)
    target_code_samsung = '{:06d}'.format(code_samsung['종목코드'].values[0])

    expr_str_sk = f"회사명=='{names_sk}'"
    code_sk = code_df.query(expr_str_sk)
    target_code_sk = '{:06d}'.format(code_sk['종목코드'].values[0])

    # 주가 데이터 가져오기
    df_samsung = web.DataReader(target_code_samsung, 'naver', start='2016-01-01', end='2023-08-29')
    df_samsung = df_samsung.astype({'Close': 'int'})

    df_sk = web.DataReader(target_code_sk, 'naver', start='2016-01-01', end='2023-08-29')
    df_sk = df_sk.astype({'Close': 'int'})

        
    return memory_df, system_df, df_sk, df_samsung

#그래프 
def plot_samsung(memory_df, system_df, df_sk, df_samsung):
    # 그래프 생성
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # 주가 그래프 선 추가
    ax1.plot(df_samsung.index, df_samsung['Close'], label='삼성전자 주가', color='blue')
    ax1.set_xlabel('연도', fontproperties=fontprop)
    ax1.set_ylabel('삼성전자 주가', color='blue', fontproperties=fontprop)
    ax1.tick_params(axis='y', labelcolor='blue')

    # 오른쪽 Y 축 생성
    ax2 = ax1.twinx()

    # memory_df 그래프 선 추가
    ax2.plot(pd.to_datetime(memory_df['년도']), memory_df['금액'], linestyle='-', marker='o' ,color='green')
    ax2.set_ylabel('', color='red', fontproperties=fontprop)
    ax2.tick_params(axis='y', labelcolor='green')

    # system_df 그래프 선 추가
    ax2.plot(pd.to_datetime(system_df['년도']), system_df['금액'], linestyle='--', marker='o', color='red')
    ax2.set_ylabel('반도체 수출입 증감률', color='green', fontproperties=fontprop)
  
    ax2.legend(['메모리', '시스템'], loc='upper left')
    
    # 그래프 스타일과 레이블 설정
    ax1.grid(True)
    ax1.set_title('주가 및 경제 지표 비교', fontproperties=fontprop)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # X 축 날짜 포맷 설정
    fig.tight_layout()

    # Streamlit에서 그래프 표시
    st.pyplot(fig)
    
#그래프 
def plot_sk(memory_df, system_df, df_sk, df_samsung):
    # 그래프 생성
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # 주가 그래프 선 추가
    ax1.plot(df_sk.index, df_sk['Close'], label='하이닉스 주가', color='blue')
    ax1.set_xlabel('연도', fontproperties=fontprop)
    ax1.set_ylabel('하이닉스 주가', color='blue', fontproperties=fontprop)
    ax1.tick_params(axis='y', labelcolor='blue')

    # 오른쪽 Y 축 생성
    ax2 = ax1.twinx()

    # memory_df 그래프 선 추가
    ax2.plot(pd.to_datetime(memory_df['년도']), memory_df['금액'], linestyle='-', marker='o' ,color='green')
    ax2.set_ylabel('', color='red', fontproperties=fontprop)
    ax2.tick_params(axis='y', labelcolor='green')

    # system_df 그래프 선 추가
    ax2.plot(pd.to_datetime(system_df['년도']), system_df['금액'], linestyle='--', marker='o', color='red')
    ax2.set_ylabel('반도체 수출입 증감률', color='green', fontproperties=fontprop)
  
    ax2.legend(['메모리', '시스템'], loc='upper left')
    
    # 그래프 스타일과 레이블 설정
    ax1.grid(True)
    ax1.set_title('주가 및 경제 지표 비교', fontproperties=fontprop)
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # X 축 날짜 포맷 설정
    fig.tight_layout()

    # Streamlit에서 그래프 표시
    st.pyplot(fig)
    
def stock_df(df_sk, df_samsung):
    st.write("삼성전자 주가 데이터:")
    st.write(df_samsung)

    st.write("SK하이닉스 주가 데이터:")
    st.write(df_sk)

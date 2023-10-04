import streamlit as st
from utils import data8_module as dm8

memory_df, system_df, df_sk, df_samsung = dm8.load_data()

def result13():
    st.subheader('삼성전자 주가 & 시스템 메모리 수출 비교')
    dm8.plot_samsung(memory_df, system_df, df_sk, df_samsung)
    
    st.subheader('SK하이닉스 주가 & 시스템 메모리 수출 비교')
    dm8.plot_sk(memory_df, system_df, df_sk, df_samsung)
    st.write('시스템 반도체 부분의 매출그래프에는 영향을 받는 부분이 2021년부터 2022년 상승하는 부분이외에는 거의 영향이 미비하다고 보여진다 \n \
             반대로 메모리 반도체 부분의 수출액에따라서 주가가 비슷한 형상으로 변화되는것을 확인 할 수 있다. \
                 즉 가격변동이 심한 메모리에따라서 주가가 많은 변동사항이 있는것을 추정할 수 있었다.')
    
def result14():
    dm8.stock_df(df_sk, df_samsung)
    
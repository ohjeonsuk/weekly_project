from utils import data3_module as dm3
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def result5():
    st.subheader('수출 반도체 내 품종별 차지 비중')
    st.write('시스템 반도체의 수출 비중이 증가하고 있는 추세지만 전체적인 흐름으로 보았을 때 전체 반도체 수출액 중 메모리 반도체가 차지하는 비중이 크다는 것을 확인할 수 있다. ')
    st.write('\n')
    df, df_year = dm3.data()
    fig = dm3.test5(df_year, '반도체(억불)', '메모리(억불)', '시스템_반도체(억불)', '개별소자(억불)')
    st.pyplot(fig)
    st.write('반도체 수출 총합 그래프의 양상이 메모리 반도체 수출 그래프와 유사하다. 또한 메모리 반도체의 수출액 그래프가 시스템 반도체의 수출액 그래프보다 상단에 위치한다. 이를 통해 메모리 시스템의 비중이 시스템 메모리보다 크다는 것을 유추해낼 수 있다.')
    st.write('\n')


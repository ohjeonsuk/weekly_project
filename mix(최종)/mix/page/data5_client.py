from utils import data5_module as dm5
import streamlit as st
import matplotlib.pyplot as plt

def result7():
    df, df4 = dm5.data2()
    fig = dm5.test7(df, df4)
    st.pyplot(fig)
    st.subheader('실질 GDP와 국내 수출액')
    st.write('실질 GDP의 성장률 그래프와 한국의 수출액 그래프의 양상이 유사한 것을 볼 수 있다. 이를 통해 한국의 수출 실적이 실질 GDP의 성장률에 큰 요인으로 작용한다는 것을 유추할 수 있다.')
    st.write('\n')

def result8():
    df2 = dm5.data2()
    fig = dm5.test8(df2)
    st.pyplot(fig)
    st.subheader('단계별 수출 품목 비중')
    st.write('수출 품목 단계별(자본재, 중간재, 소비재, 1차 산품, 기타) 비중을 그래프를 통해 확인할 수 있다. 중간재의 비중이 가장 크며 이는 곧 중간재의 수출 실적이 실질 GDP에 큰 영향을 끼친다는 것을 근거할 수 있는 데이터가 된다.')
    st.write('\n')

def result9():
    col1, col2 = st.columns([3.5, 1.5])
    with col1:
        fig = dm5.test9()
        st.pyplot(fig)
    with col2:
        st.write('수출 품목별 수출액 증감룰을 보면 중간재의 증감율의 폭이 큰 것과, 최근 중간재의 수출액은 감소하고 있는 것을 확인할 수 있다. 이전 페이지에서 수출 품목 중 반도체가 큰 비중을 차지하는 것을 확인했다. 즉, 반도체의 수출 실적이 결과적으로 GDP에 큰 영향을 미친다는 것을 확인할 수 있다.')
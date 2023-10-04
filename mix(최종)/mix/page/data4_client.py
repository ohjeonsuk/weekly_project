import streamlit as st
from utils import data4_module as dm4
import matplotlib.pyplot as plt

def result6():
    col1, col2 = st.columns([3.2, 1.8])
    with col1:
        df, df1 = dm4.data1()
        fig = dm4.test6(df, df1)
        st.pyplot(fig)
    with col2:
        file_path = '산업통상자원부_반도체디스플레이 수출동향 추이_20221231.csv'
        list = ['년월','메모리_전년동월대비_증감률(퍼센트)','시스템_반도체_전년동월대비_증감률(퍼센트)']
        fig = dm4.test7(file_path, list)
        plt.grid(False)
        st.pyplot(fig)
    st.subheader('시스템과 메모리 반도체의 가격변동성 차이')
    st.write('메모리 반도체와 시스템 반도체의 수출액 추이 그리고 두 반도체의 전년동월대비 수출액 증감율 그래프를 도출해보았다. 두 그래프에서 공통적으로 확인할 수 있는 점은 메모리 반도체의 가격 변동성이 시스템 반도체의 가격 변동성보다 크다는 것이다.')

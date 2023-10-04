from utils import data2_module as dm2
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def result3():
    col1, col2 = st.columns([3.5, 1.5])
    with col1:
        overall_ratios = [0.327, 0.159, 0.137, 0.071, 0.059, 0.057, 0.054, 0.048, 0.046, 0.044]
        labels = ["반도체", "석유제품", "자동차", "합성수지", "자동차부품", "철강판", "평판디스플레이및센서","정밀화학원료", "선박해양구조물및부품", "무선통신기기"]
        age_ration = [0.037, 0.393, 0.57]
        age_labels = ['개별소자', '시스템 반도체', '메모리 반도체']
        fig = dm2.test3(overall_ratios,labels,age_ration,age_labels)
        st.pyplot(fig)
    with col2:
        data = {'순위':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], '품목': ['반도체', '석유제품', '자동차', '합성수지', '자동차 부품', '철강판', '평판디스플레이', '정밀화학원료', '선박해양구조물', '무선통신기기']}
        df = pd.DataFrame(data)
        df.set_index('순위', inplace = True)
        st.table(df)

def result4():
    st.subheader('국내 수출 품목 비중')
    st.write('한국의 수출 품목을 수출액 기준으로 하여 순위를 매겨보았다. 한국의 수출 품목 중 32.6%의 비중을 차지하는 반도체가 1위, 그 아래로 석유제품, 자동차, 합성수지, 자동차 부품, 철강판, 평판 디스플레이, 정밀 화학 원료, 선박 해양 구조물, 무선통신기기의 순서대로 비중이 컸다. ')
    st.write('\n')
    file_path = '산업통상자원부_반도체디스플레이 수출동향 추이_20221231.csv'
    sns.set_style('whitegrid')
    fig = dm2.test4(file_path)
    st.pyplot(fig)

 
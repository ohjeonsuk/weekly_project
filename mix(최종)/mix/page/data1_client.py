from utils import data1_module as dm1
import streamlit as st
import matplotlib.pyplot as plt

def result1():
    col1, col2 = st.columns([2.5, 2.5])
    with col1:
        file_path = '국가별 반도체 수출.csv'
        country_list = ['China', 'China, Hong Kong SAR', 'Singapore', 'Rep. of Korea']
        df = dm1.test1(file_path, country_list)  # 데이터프레임을 받아옴
        plt.figure(figsize=(8, 5))
        plt.rcParams['font.family'] = 'NanumGothic'
        for country in df.columns:
            plt.plot(df.index, df[country], label=country)

        plt.ylabel('Export Growth Rate (%)')
        plt.title('반도체 주요 수출국의 반도체 수출 증감율', fontsize = 18)
        plt.text(0, -0.1, '출처: UN Comtrade', fontsize=8, color='gray', transform=plt.gca().transAxes)
        plt.subplots_adjust(bottom=0.2)
        plt.legend()
        plt.grid(True)
        st.pyplot(plt)
    with col2:
        centered_text = """
    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
        <p style="text-align: center;">이 텍스트는 중앙 정렬됩니다.</p>
    </div>
"""
        st.subheader('국가별 반도체 수출 증감율')
        st.write('반도체 주요 수출국의 반도체 수출액 증감률을 그래프로 나타내 보았을 때, 한국의 수출액 증감폭이 타국에 비해 크다는 것을 볼 수 있다. 이를 통해 글로벌 IT 경기순환 요인 외, 한국의 시장 구조가 국내 반도체 시장에 영향을 미친 가능성에 대해 분석해보고자 한다.')
        st.write('\n')
    st.write('한국와 홍콩의 수출 증감률을 비교하여 파란 영역으로, 싱가포르와 홍콩의 수출 증감율 비교하여 빨간 영역으로 표현해보았다. 한 눈에 보이듯이 한국과 타국의 수출 증감율 차이가 다른 두 국가를 비교했을 때의 차이보다 큰 것을 확인할 수 있다.')
    st.write('\n')
def result2():
    file_path = '국가별 반도체 수출.csv'
    country_list = ['China', 'China, Hong Kong SAR', 'Singapore', 'Rep. of Korea']
    df = dm1.test1(file_path, country_list)
    fig = dm1.test2(df)
    st.pyplot(fig)

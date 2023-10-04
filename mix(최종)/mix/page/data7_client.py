from utils import data7_module as dm7
import streamlit as st
import os 

path = os.path.dirname(__file__)
parent_path = os.path.dirname(path)
utils_path = os.path.join(parent_path, 'utils')
file_path = os.path.join(utils_path, 'data')

#국가별 반도체 막대그래프
def result11():
    category_names = ['System', 'Memory']
    results = {
        'China, Hong Kong SAR': (81289921398, 37643977488),
        'China': (52263191419, 70297732758),
        'Singapore': (50363164992, 18327631158),
        'Rep. of Korea': (38402894055, 61777688705),
        'USA': (29658200748, 2449735145),
        'Ohter Asia, nes': (15395171041, 21750120655)}
    fig, ax = dm7.survey(results, category_names)
    st.pyplot(fig)
    st.subheader('2022년 국가별 반도체 수출액')
    st.write('2022년 대표 국가들의 반도체 시스템과 메모리의 매출액 비교 \n \
         특수한 중국을 빼놓고 한국을 제외하면 시스템 반도체의 수출 비중이 높은걸 확인했다. \
         중국의경우는 팹리스의 회사들을 비롯 균형있게 수출액이 나오고 있지만, 값싼 노동력을 이용한 공장이 메인이라 자체적인 성과는 적은편이다.')
         
 
def result12():
    grouped = dm7.data()
    fig = dm7.plot_data(grouped)
    st.pyplot(fig)
    st.write('한국만 유독 변화율이 심하편인데 이것이 즉 메모리에 가격변동에따른 영향을 많이 받는다고 볼 수 있다. \
             또한 상위권의 나라들이 전부 시스템 반도체 비중이 높은 것을 주목할만하다.')
    st.write('\n')
    
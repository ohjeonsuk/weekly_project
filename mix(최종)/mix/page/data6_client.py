from utils import data6_module as dm6
import streamlit as st
import matplotlib.pyplot as plt

def result10():
    fig = dm6.test10()
    st.pyplot(fig)
    st.subheader('메모리 반도체 수요 분야')
    st.write('국내 수출 반도체의 수요 분야에 대해 메모리 시스템을 집중적으로 분석해보았다. 메모리 반도체 수요 분야는 모바일보단 서버의 수요가 높다. 하지만 메모리 반도체 자체의 수요가 감소하는 추세이기 때문에 2022년 이후의 그래프는 우하향하는 것을 볼 수 있다.')
    st.write('\n')
    fig = dm6.test11()
    st.pyplot(fig)
    st.subheader('스마트폰 출하량')
    st.write('다음은 스마트폰 출하량에 대해 그래프로 나타낸 것이다. 점으로 표시한 각 그래프의 고점을 보면, 그 고점의 높이가 점점 낮아지고 있는 것을 확인할 수 있다. 즉, 스마트폰의 교체 주기가 점점 늘어나고 있다. 이는 위에서 분석한 모바일의 메모리 반도체 수요가 서버보다 낮다는 것의 근거가 될 수 있다.')
    st.write('\n')
    fig = dm6.test12()
    st.pyplot(fig)
    st.subheader('서버용 D램과 모바일용 D램의 생산량 추이')
    st.write('다음은 서버용 D램과 모바일용 D램의 생산량 추이에 대해 비교해본 것이다. 서버용 D램이 모바일용 D램의 생산량을 따라잡은 것을 확인할 수 있다.')

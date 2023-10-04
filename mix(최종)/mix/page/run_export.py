from utils import export as ep
from utils import module as md
import streamlit as st


def app():
    st.header('반도체 수출')
    
    fig = md.sidexport(ep.df_year_)
    st.pyplot(fig)
    st.write('반도체 수출 금액과 각 항목이 차지하는 부분을 나타내봤습니다.')
    st.write('2019년, 2020년에 수출액이 줄어든건 미국-중국 간의 무역전쟁으로 인한 여파라고 예상합니다.'
             ' 각 항목이 차지는 비율을 살펴보면 메모리가 우리나라 반도체 수출의 주력 상품이지만 2022년 들어서서는 시스템 반도체가 많이 따라왔다는걸 알 수 있습니다.')
    
    
    fig = md.exportplot(ep.df_year_, '반도체(억불)', '메모리(억불)', '시스템_반도체(억불)', '개별소자(억불)')
    st.pyplot(fig)
    st.write('주력 상품인 메모리의 수출액에 따라 반도체 수출액도 비슷하게 변하는걸 알 수 있고'
             ' 2022년에 메모리 수출액이 감소 하였지만 시스템 반도체 수출액이 증가 하여'
             ' 반도체 수출액에는 큰 변화가 없는것으로 보입니다.')
    
    fig = md.memoryratio(ep.df_year_)
    st.pyplot(fig)
    st.write('메모리 수출액에서 D램, 낸드, MCP가 차지하는 비율을 알아보기위해 그래프로 나타냈습니다.'
         ' 그런데 D램, 낸드, MCP의 총합이 메모리 수출액과 맞지 않는 부분이 있어 나머지 금액은'
         ' 기타로 처리했습니다.')
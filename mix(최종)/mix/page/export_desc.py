from utils import export as ep
import streamlit as st
import io


def app():
    url_export = 'https://www.data.go.kr/data/15051126/fileData.do'
    
    st.header('반도체 수출')
    st.markdown(f'출처 : {url_export}')
    
    st.dataframe(ep.df_main)
    
    buffer = io.StringIO()
    ep.df_main.info(buf=buffer)
    info_str = buffer.getvalue()
    
    with st.expander("반도체 수출 Info"):
        st.text(info_str)
    
    st.write('데이터를 확인해보면 2015년 1월 ~ 2022년 12월 까지의 반도체 수출 데이터이고 항목으로는 반도체'
             ', 메모리(D램 + 낸드 + MCP), 시스템 반도체, 개별소자, 디스플레이가 있습니다. info로는 년월 부분이 시간 데이터가 아니고 나머지는  실수 데이터임을 알 수 있습니다.')
    
    st.dataframe(ep.df_year)
    st.write('년월 부분을 시간 데이터로 바꿔주고 인덱스로 보낸 다음 월 별로 나눠져 있는 데이터를 연도별로 합쳐주면서 실수 데이터 부분은 모두 더해주었습니다.')
    st.dataframe(ep.df_year_)
    st.write('증감률 항목들은 연도를 기준으로 더해주면서 의미가 없어져 버리고 디스플레이는 반도체가 아니라서 버렸습니다.')
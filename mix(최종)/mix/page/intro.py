import streamlit as st
import pandas as pd

def app():
    custom_style = """
        <style>
            .custom-header {
                font-size: 42px;
                color: black;
                text-align: center;
            }
        </style>
    """

    # HTML 코드를 Markdown 형식으로 렌더링
    st.markdown(custom_style, unsafe_allow_html=True)
    st.markdown("<p class='custom-header'><strong>반도체 수출 동향을 통한 국내 반도체 시장 분석</strong></p>", unsafe_allow_html=True)


    centered_text_with_style = """
    <div style="display: flex; justify-content: center; align-items: center; height: 200px;">
        <p style="text-align: center; font-size: 25px; color: black;">
                   <strong>주간프로젝트 2조</strong><br>
            팀원
        </p>
    </div>
    """

    # HTML 코드를 Markdown 형식으로 렌더링
    st.markdown(centered_text_with_style, unsafe_allow_html=True)


    mem = pd.DataFrame({
        '조원': ['조장', '조원', '조원', '조원'],
        '이름': ['최서진', '김기인', '권용현', '오전석']
    }).set_index('조원')

    st.table(mem)

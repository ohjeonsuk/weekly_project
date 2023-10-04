import streamlit as st

def desc():
    image_path = './class_diagram.jpg'
    st.image(image_path, caption='[Class 다이어그램]', use_column_width=True)
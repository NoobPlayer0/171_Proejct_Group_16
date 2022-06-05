import streamlit as st
from alcoholPredict import show_predict_page

with st.sidebar:
    st.title('@Some selection codes@')

    st.header('Sex')
    st.text('0 - Female  1 - Male')

    st.header('Family Size')
    st.text('0 - Less than or equal to 3')
    st.text('1 - Greater than 3')

    st.header('Mother(Father) Education Level')
    st.text('0 - none')
    st.text('1 - primary education (4th grade)')
    st.text('2 - 5th to 9th grade')
    st.text('3 - secondary education')
    st.text('4 - higher education')

    st.header("Mother(Father)'s Job")
    st.text('0 - teacher')
    st.text('1 - health')
    st.text('2 - services')
    st.text('3 - at home')
    st.text('4 - other')

    st.header('Weekly Study Time')
    st.text('0 - <2 hours')
    st.text('1 - 2 to 5 hours')
    st.text('2 - 5 to 10 hours')
    st.text('3 - >10 hours')

    st.header('Age')
    st.text('0 - 15')
    st.text('1 - 16')
    st.text('2 - 17')
    st.text('3 - 18')
    st.text('4 - 19')
    st.text('5 - 20')
    st.text('6 - 21')
    st.text('7 - 22')

# if page == "Predict":

show_predict_page()
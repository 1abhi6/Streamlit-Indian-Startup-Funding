"""Streamlit App
Keyword arguments:
argument -- description
Return: return_description
"""


import streamlit as st

from analysis import Investor
from analysis import Startup

investor = Investor()


st.sidebar.title('Startup Funding analysis')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',['Ola','Unacademy'])
    btn1 = st.sidebar.button('Find Startup details')
    st.title('Startup Analysis')
elif option == 'Investor':
    st.sidebar.selectbox('Select Startup',investor.investor_list())
    btn1 = st.sidebar.button('Find Investor details')
    st.title('Investor Analysis')
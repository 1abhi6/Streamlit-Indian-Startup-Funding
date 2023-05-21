"""Streamlit App
Keyword arguments:
argument -- description
Return: return_description
"""


import streamlit as st
import pandas as pd
import matplotlib as plt



df = pd.read_csv('dataset/startup_funding.csv')

# data cleaning
df['Investors Name'] = df['Investors Name'].fillna('Undisclosed')

st.sidebar.title('Startup Funding analysis')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',sorted(df['Startup Name'].unique().tolist()))
    btn1 = st.sidebar.button('Find Startup details')
    st.title('Startup Analysis')
elif option == 'Investor':
    st.sidebar.selectbox('Select Startup',sorted(df['Investors Name'].unique().tolist()))
    btn1 = st.sidebar.button('Find Investor details')
    st.title('Investor Analysis')
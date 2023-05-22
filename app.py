"""Streamlit App
Keyword arguments:
argument -- description
Return: return_description
"""


import streamlit as st

from analysis import Investor as InvestorAnalysis
from analysis import Startup as StartupAnalysis
from components import Investor as InvestorComponent


investor_analysis = InvestorAnalysis()
investor_component = InvestorComponent()
st.sidebar.title('Startup Funding analysis')
option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

if option == 'Overall Analysis':
    st.title('Overall Analysis')
elif option == 'Startup':
    st.sidebar.selectbox('Select Startup',['Ola','Unacademy'])
    btn1 = st.sidebar.button('Find Startup details')
    st.title('Startup Analysis')
elif option == 'Investor':
    investor_name = st.sidebar.selectbox('Select Startup',investor_analysis.investor_list())
    btn1 = st.sidebar.button('Find Investor details')
    st.title('Investor Detail')
    if btn1:
        investor_component.five_most_recent_investments(investor_name)
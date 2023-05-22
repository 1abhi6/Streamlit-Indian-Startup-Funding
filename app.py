"""Streamlit App
Keyword arguments:
argument -- description
Return: return_description
"""

import streamlit as st

from analysis import Investor as InvestorAnalysis
from components import Investor as InvestorComponent

class Main:
    def __init__(self) -> None:
        self.investor_analysis = InvestorAnalysis()
        self.investor_component = InvestorComponent()
        self.home_component()

    def home_component(self):
        # Page configuration
        st.set_page_config(layout='wide',page_title="Abhi's Startup Analysis",page_icon='📊')
        st.sidebar.title('Startup Funding analysis')
        option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

        if option == 'Overall Analysis':
            st.title('Overall Analysis')
        elif option == 'Startup':
            st.sidebar.selectbox('Select Startup',['Ola','Unacademy'])
            btn1 = st.sidebar.button('Find Startup details')
            st.title('Startup Analysis')
        elif option == 'Investor':
            investor_name = st.sidebar.selectbox('Select Startup',self.investor_analysis.investor_list())
            btn1 = st.sidebar.button('Find Investor details')
            st.title('Investor Detail')
            if btn1:
                self.investor_component.recent_five_investments(investor_name)
                col1 , col2 = st.columns(2)
                with col1:
                    self.investor_component.plot_biggest_investment(investor_name)
                with col2:
                    self.investor_component.plot_invested_sector(investor_name)
Main()
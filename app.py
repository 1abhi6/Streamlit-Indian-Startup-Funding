import streamlit as st

from analysis import Investor as InvestorAnalysis
from components import Investor as InvestorComponent
from components import padding_top

class Main:
    def __init__(self) -> None:
        self.investor_analysis = InvestorAnalysis()
        self.investor_component = InvestorComponent()
        self.home_component()
        

    def home_component(self):
        # Page configuration
        st.set_page_config(layout='wide',page_title="Abhi's Startup Analysis",page_icon='📊')
        st.sidebar.title('Startup Funding analysis',help='Note: This data used for this analysis about investment in Indian startups between 2015 to 2020')
        option = st.sidebar.selectbox('Select One',['Overall Analysis','Startup','Investor'])

        if option == 'Overall Analysis':
            st.title('Overall Analysis')
        elif option == 'Startup':
            st.sidebar.selectbox('Select Startup',['Ola','Unacademy'])
            btn1 = st.sidebar.button('Find Startup details')
            st.title('Startup Analysis')
        elif option == 'Investor':
            self.investor()
    
    def investor(self):
        investor_name = st.sidebar.selectbox('Select Startup',self.investor_analysis.investor_list())
        st.markdown(padding_top, unsafe_allow_html=True)
        btn = st.sidebar.button('Find Investor details')
        st.markdown("<h1 style='text-align: center; color: white;'>Investor Detail</h1>", unsafe_allow_html=True)
        st.title(investor_name)
        st.divider()
        if btn:
            self.investor_component.recent_five_investments(investor_name)
            st.divider()

            col1 , col2 = st.columns(2)
            with col1:
                self.investor_component.plot_biggest_investment(investor_name)
            with col2:
                self.investor_component.plot_invested_city(investor_name)
            st.divider()

            col3 , col4 = st.columns(2)
            with col3:
                self.investor_component.plot_invested_sector(investor_name)
            with col4:
                self.investor_component.plot_invested_subsector(investor_name)
            st.divider()
                
            col5 , col6 = st.columns(2)
            with col5:
                self.investor_component.plot_invested_type(investor_name)
            with col6:
                self.investor_component.plot_yoy_investment(investor_name)
            st.divider()
            self.investor_component.get_similar_investors(investor_name)
                    
Main()
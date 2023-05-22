import streamlit as st

# from dataset import startup

from analysis import Investor as InvestorAnalysis


class Investor:
    def __init__(self):
        # self.startup = startup
        self.investor_analysis = InvestorAnalysis()
   
    def five_most_recent_investments(self,investor_name):
        st.title(investor_name)
        st.subheader('Most Recent Investments')
        st.dataframe(self.investor_analysis.recent_five_investments(investor_name))

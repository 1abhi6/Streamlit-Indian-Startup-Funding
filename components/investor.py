import streamlit as st
import matplotlib.pyplot as plt

from analysis import Investor as InvestorAnalysis


class Investor:
    def __init__(self):
        self.investor_analysis = InvestorAnalysis()
   
    def recent_five_investments(self,investor_name):
        st.title(investor_name)
        st.subheader('Most Recent Investments')
        st.dataframe(self.investor_analysis.recent_five_investments(investor_name))
    
    def plot_biggest_investment(self,investor_name):
        st.title(investor_name)
        st.subheader('Biggest Investments')
        biggest_series = self.investor_analysis.biggest_investment(investor_name)
        fig, axis = plt.subplots()
        axis.bar(biggest_series.index,biggest_series.values)
        st.pyplot(fig)
    
    def plot_invested_sector(self,investor_name):
        st.title(investor_name)
        st.subheader('Sector Invested in')
        sector_series = self.investor_analysis.invested_sector(investor_name)
        fig,axis = plt.subplots()
        axis.pie(sector_series,labels=sector_series.index,autopct="%0.01f%%")
        st.pyplot(fig)
    
    def plot_invested_city(self,investor_name):
        st.title(investor_name)
        st.subheader('City Invested in')
        city_series = self.investor_analysis.invested_city(investor_name)
        fig,axis = plt.subplots()
        axis.pie(city_series,labels=city_series.index,autopct="%0.01f%%")
        st.pyplot(fig)

    def plot_invested_type(self,investor_name):
        st.title(investor_name)
        st.subheader('Investment Type')
        type_series = self.investor_analysis.invested_type(investor_name)
        fig,axis = plt.subplots()
        axis.pie(type_series,labels=type_series.index,autopct="%0.01f%%")
        st.pyplot(fig)
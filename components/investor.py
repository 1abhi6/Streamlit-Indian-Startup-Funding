import streamlit as st
import plotly.express as px

from analysis import Investor as InvestorAnalysis


class Investor:
    def __init__(self):
        self.investor_analysis = InvestorAnalysis()
   
    def recent_five_investments(self,investor_name):
        st.subheader('Most Recent Investments',help=f"{investor_name}'s five most recent investments.")
        st.dataframe(self.investor_analysis.recent_five_investments(investor_name))
    
    def plot_biggest_investment(self,investor_name):
        st.subheader('Biggest Investments',help=f"{investor_name}'s biggest investments in terms of amount.")
        biggest_investment_df = self.investor_analysis.biggest_investment(investor_name)
        fig = px.bar(biggest_investment_df, x='name', y='amount')
        st.plotly_chart(fig,use_container_width=True)
    
    def plot_invested_sector(self,investor_name):
        st.subheader('Sector Invested in',help=f"{investor_name}'s most invested sector.")
        sector_df = self.investor_analysis.invested_sector(investor_name)
        fig = px.pie(sector_df, values='amount', names='vertical')
        st.plotly_chart(fig,use_container_width=True)

    def plot_invested_subsector(self,investor_name):
        st.subheader('Sector Invested in',help=f"{investor_name}'s most invested subsector.")
        subsector_df = self.investor_analysis.invested_subsector(investor_name)
        fig = px.pie(subsector_df, values='amount', names='subvertical')
        st.plotly_chart(fig,use_container_width=True)
    
    def plot_invested_city(self,investor_name):
        st.subheader('City Invested in',help=f"{investor_name}'s most invested city.")
        city_df = self.investor_analysis.invested_city(investor_name)
        fig = px.pie(city_df, values='amount', names='city')
        st.plotly_chart(fig,use_container_width=True)

    def plot_invested_type(self,investor_name):
        st.subheader('Investment Type',help=f"{investor_name}'s stage of investments.")
        investment_type_df = self.investor_analysis.invested_type(investor_name)
        fig = px.pie(investment_type_df, values='amount', names='type')
        st.plotly_chart(fig,use_container_width=True)
    
    def plot_yoy_investment(self,investor_name):
        st.subheader('YOY investment',help=f"{investor_name}'s year on year investments.")
        yoy_investment_df = self.investor_analysis.yoy_investment(investor_name)
        fig = px.line(yoy_investment_df, x="year", y="amount")
        st.plotly_chart(fig,use_container_width=True)

import streamlit as st
import plotly.express as px

from analysis import Overall as OverallAnalysis

class Overall:

    def __init__(self):
        self.overall_analysis = OverallAnalysis()

    def plot_total_funding_mom(self):
        temp_df = self.overall_analysis.total_funding_mom()
        st.subheader('Total Amount of Funding in Indian Startups MoM',help='Total Amount of Funding in Indian Startups on the basis of month and year')
        fig = px.line(temp_df, x='MM-YYYY', y='Total Funding (In Crore Rs.)', title='Total funding in Startups in MM-YYYY')
        st.plotly_chart(fig,use_container_width=True)

    def plot_total_funded_startup_mom(self):
        temp_df = self.overall_analysis.total_funded_startup_mom()
        st.subheader('Total Funded Indian Startups MoM',help='Total Funded Indian Startups on the basis of month and year')
        fig = px.line(temp_df, x='MM-YYYY', y='Total Funded Startups',title='Total Funded Startups in MM-YYYY')
        st.plotly_chart(fig,use_container_width=True)
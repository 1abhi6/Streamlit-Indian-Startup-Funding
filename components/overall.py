import streamlit as st
import plotly.express as px

from analysis import Overall as OverallAnalysis

class Overall:

    def __init__(self):
        self.overall_analysis = OverallAnalysis()

    def total_funding_mom(self):
        temp_df = self.overall_analysis.total_funding_mom()
        fig = px.line(temp_df, x='MM-YYYY', y='Total Funding (In Crore Rs.)', title='Total Amount of Funding in Startups in MM-YYYY')
        st.plotly_chart(fig,use_container_width=True)
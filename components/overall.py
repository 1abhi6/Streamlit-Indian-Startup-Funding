import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from analysis import Overall as OverallAnalysis


class PlotHorizontalBarChart:
    def __init__(self,x_axis:pd.Series,y_axis:pd.Series,layout_title,layout_x_axis:str,layout_yaxis:str) -> None:
        fig = go.Figure(data=go.Bar(
            x=x_axis,
            y=y_axis,
            orientation='h'
        ))

        fig.update_layout(
            title=layout_title,
            xaxis=dict(title=layout_x_axis),
            yaxis=dict(title=layout_yaxis)
        )

        st.plotly_chart(fig,use_container_width=True)
    
class PlotLineChart:
    def __init__(self,temp_df:str,x_axis:str,y_axis:str,layout_title:str) -> None:
        fig = px.line(
            temp_df,
            x=x_axis,
            y=y_axis,
            title=layout_title
        )

        st.plotly_chart(fig,use_container_width=True)

class SubHeader:
    def __init__(self,title:str,tooltip:str) -> None:
        st.subheader(title, help=tooltip)

class Overall:
    def __init__(self) -> None:
        self.overall_analysis = OverallAnalysis()

    def plot_total_funding_mom(self):
        temp_df = self.overall_analysis.total_funding_mom()

        SubHeader(
            title='Total Amount of Funding in Indian Startups MoM',
            tooltip='Total Amount of Funding in Indian Startups on the basis of month and year'
        )

        PlotLineChart(
            temp_df=temp_df,
            x_axis='MM-YYYY',
            y_axis='Total Funding (In Crore Rs.)',
            layout_title='Total funding in Startups in MM-YYYY'
        )

    def plot_total_funded_startup_mom(self):
        temp_df = self.overall_analysis.total_funded_startup_mom()

        SubHeader(
            title='Total Funded Indian Startups MoM',
            tooltip='Total Funded Indian Startups on the basis of month and year'
        )

        PlotLineChart(
            temp_df=temp_df,
            x_axis='MM-YYYY',
            y_axis='Total Funded Startups',
            layout_title='Total Funded Startups in MM-YYYY'
        )

    def plot_most_funded_sector(self):
        most_funded_sectors = self.overall_analysis.most_funded_sector()

        SubHeader(
            title='Most Funded Sectors',
            tooltip='Top 10 Most Funded Sectors between 2015 to 2020'
        )

        PlotHorizontalBarChart(
            x_axis=most_funded_sectors['amount'],
            y_axis=most_funded_sectors['vertical'],
            layout_title='Top 10 Most Funded Sectors',
            layout_x_axis='Funding Amount (In Crore Rs)',
            layout_yaxis='Sector'
        )

    def plot_most_funded_type(self):
        most_funded_type = self.overall_analysis.most_funded_type()

        SubHeader(
            title='Most Funded Type',
            tooltip='Top 10 most funded type of round in startup funding'
        )

        PlotHorizontalBarChart(
            x_axis=most_funded_type['amount'],
            y_axis=most_funded_type['type'],
            layout_title='Top 10 Most Funded Types of Rounds',
            layout_x_axis='Funding Amount (In Crore Rs)',
            layout_yaxis='Type of Investment'
        )

    def plot_most_funded_cities(self):
        most_funded_city = self.overall_analysis.most_funded_cities()

        SubHeader(
            title='Most Funded Cities',
            tooltip='Top 10 most funded cities in startup funding'
        )

        PlotHorizontalBarChart(
            x_axis=most_funded_city['amount'],
            y_axis=most_funded_city['city'],
            layout_title='Most Funded Cities',
            layout_x_axis='Funding Amount (In Crore Rs)',
            layout_yaxis='City'
        )

    def plot_most_funded_startups_yoy(self):
        most_funded_startup_yoy = self.overall_analysis.most_funded_startups_yoy()

        SubHeader(
            title='Most Funded Startups YoY',
            tooltip='Top 10 most funded startups in startup funding YoY'
        )

        fig = px.bar(
            most_funded_startup_yoy,
            x='StartUp Name',
            y='Amount (In Crore Rs)',
            color='Year'
        )

        st.plotly_chart(fig,use_container_width=True)


import streamlit as st
from analysis import Startup as StartupAnalysis

class Startup:
    def __init__(self) -> None:
        self.startup_analysis = StartupAnalysis()

    def similar_startups(self, startup_name):
            
            similar_startups = self.startup_analysis.similar_startups(startup_name)
            st.subheader(
                'Similar Startups',
                help=f"These startups belongs from the same sector as {startup_name}."
            )
            st.write('')
            col0, col1, col2, col3 = st.columns(4)
            with col0:
                try:
                    st.write(similar_startups[0])
                except IndexError:
                    st.write('')
            with col1:
                try:
                    st.write(similar_startups[1])
                except IndexError:
                    st.write('')
            with col2:
                try:
                    st.write(similar_startups[2])
                except IndexError:
                    st.write('')
            with col3:
                try:
                    st.write(similar_startups[3])
                except IndexError:
                    st.write('')
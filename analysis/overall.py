import pandas as pd
import numpy as np

from dataset import startup

class Overall:
    def __init__(self):
        self.startup = startup


    
    def total_funding_mom(self):
        temp_df = startup.groupby(['year','month'])['amount'].sum().reset_index()
        temp_df['MM-YYYY'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
        temp_df.rename(columns = {
            'amount' : 'Total Funding (In Crore Rs.)'
        },inplace=True)

        return temp_df
    
    def total_funded_startup_mom(self):
        temp_df = startup.groupby(['year','month'])['amount'].count().reset_index()
        temp_df['MM-YYYY'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')
        temp_df.rename(columns = {
            'amount' : 'Total Funded Startups'
        },inplace=True)

        return temp_df

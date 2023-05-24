import pandas as pd
import numpy as np

from dataset import startup

class Overall:
    def __init__(self):
        self.startup = startup

    def total_funding_mom(self):
        self.temp_df = startup.groupby(['year','month'])['amount'].sum().reset_index()
        self.temp_df['MM-YYYY'] = self.temp_df['month'].astype('str') + '-' + self.temp_df['year'].astype('str')
        self.temp_df.rename(columns = {
            'amount' : 'Total Funding (In Crore Rs.)'
        },inplace=True)

        return self.temp_df
    
    def number_of_funding_mom(self):
        pass
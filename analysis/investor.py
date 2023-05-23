import pandas as pd
import itertools
import random

from dataset import startup
class Investor:
    def __init__(self):
        self.startup = startup
    
    # Returns the investor list
    def investor_list(self):
        return sorted(set(self.startup['investors'].str.split(',').sum()))[2:]
    
    # 5 recent investments of any Investor
    def recent_five_investments(self,investor_name):
        recent_investment = self.startup[self.startup['investors'].str.contains(investor_name)].head()[['date','name','vertical','city','investors','type','amount']].rename(columns = {
            'date':'Date of Investment',
            'name':'Startup Name',
            'vertical':'Vertical',
            'city':'City',
            'investors':'Investors',
            'type':'Type',
            'amount':'Amount'
        })

        return recent_investment
   
    # Highest investment made by an Investor
    def biggest_investment(self,investor_name):
        return self.startup[self.startup['investors'].str.contains(investor_name)].groupby('name')['amount'].sum().sort_values(ascending=False).head().reset_index()
    
    # Sector invested in
    def invested_sector(self,investor_name):
        return startup[startup['investors'].str.contains(investor_name)].groupby('vertical')['amount'].sum().reset_index()
    
    # Sub Sector invested in
    def invested_subsector(self,investor_name):
        return startup[startup['investors'].str.contains(investor_name)].groupby('subvertical')['amount'].sum().reset_index()
    
    # City invested in
    def invested_city(self,investor_name):
        return startup[startup['investors'].str.contains(investor_name)].groupby('city')['amount'].sum().reset_index()
    
    # Type of investment
    def invested_type(self,investor_name):
        return startup[startup['investors'].str.contains(investor_name)].groupby('type')['amount'].sum().reset_index()
    
    # Year on year investment
    def yoy_investment(self,investor_name):
        return startup[startup['investors'].str.contains(investor_name)].groupby('year')['amount'].sum().reset_index()
    
    # Get similar investors
    def get_similar_investors(self, investor_name):
        # Filter the dataframe based on the investor name
        investor_df = startup[startup['investors'].str.contains(investor_name)]

        if investor_df.empty:
            # No matching rows found for the investor name
            return pd.Series()

        # Get the vertical of the investor
        investor_vertical = investor_df['vertical'].iloc[0]

        # Filter the dataframe based on the vertical and exclude undisclosed investors
        vertical_df = self.startup[(self.startup['vertical'] == investor_vertical) &
                                (~self.startup['investors'].str.contains('Undisclosed Investors', case=False))]

        # Exclude the investor from the list
        vertical_df = vertical_df[vertical_df['investors'] != investor_name]

        # Count the occurrences of each investor
        # print(sorted(vertical_df['investors'].str.split(','))[:5])
        nested_list = sorted(vertical_df['investors'].str.split(','))
        flattened_list = list(itertools.chain.from_iterable(nested_list))
        try:
            return random.sample(flattened_list, 3)
        except ValueError:
            return flattened_list
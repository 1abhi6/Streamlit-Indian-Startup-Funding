import pandas as pd
import numpy as np

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
        return self.startup[self.startup['investors'].str.contains(investor_name)].groupby('name')['amount'].sum().sort_values(ascending=False).head()
    
    # Sector invested in
    def invested_sector(self,investor_name):
        return startup[startup['investors'].str.contains(investor_name)].groupby('vertical')['amount'].sum()
    
    # City invested in
    def invested_city(self,investor_name):
        return startup[startup['investors'].str.contains(investor_name)].groupby('city')['amount'].sum()
    
    def invested_type(self,investor_name):
            return startup[startup['investors'].str.contains(investor_name)].groupby('type')['amount'].sum()
    

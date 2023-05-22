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
    def recent_five_investments(self):
        recent_investment = self.startup[self.startup['investors'].str.contains(' IDG Ventures')].head()[['date','name','vertical','city','investors','type','amount']].rename(columns = {
            'date':'Date of Investment',
            'name':'Startup Name',
            'vertical':'Vertical',
            'city':'City',
            'investors':'Investors',
            'type':'Type',
            'amount':'Amount'
        })

        return recent_investment


import pandas as pd
import numpy as np

from dataset import startup

class Overall:
    def __init__(self):
        self.startup = startup

    def total_invested_amount(self):
        return round(self.startup['amount'].sum())

    def max_amount_infused(self):
        return self.startup.groupby('name')['amount'].max().sort_values(ascending=False).head(1).values[0]

    def avg_ticket_size(self):
        return self.startup.groupby('name')['amount'].sum().mean()

    def total_funded_startup(self):
        return self.startup['name'].nunique()

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
    
    def most_funded_sector(self):
        temp_df = startup.groupby('vertical')['amount'].sum().reset_index()
        most_funded_sectors = temp_df[temp_df['amount'] != 0.0].sort_values(by='amount',ascending=False).head(10)
        most_funded_sectors['amount'] = round(most_funded_sectors['amount'],2)

        return most_funded_sectors
    
       
    def most_funded_type(self):
        temp_df = startup.groupby('type')['amount'].sum().reset_index()
        most_funded_type = temp_df[temp_df['amount'] != 0.0].sort_values(by='amount',ascending=False).head(10)

        return most_funded_type
    
    def most_funded_cities(self):
        temp_df = startup.groupby('city')['amount'].sum().reset_index()
        most_funded_city = temp_df[temp_df['amount'] != 0]

        # Add the amount of Bengaluru to Bangalore
        most_funded_city.loc[most_funded_city['city'] == 'Bangalore', 'amount'] += most_funded_city.loc[most_funded_city['city'] == 'Bengaluru', 'amount'].values[0]

        # Drop the Bengaluru row
        most_funded_city = most_funded_city[most_funded_city['city'] != 'Bengaluru']

        most_funded_city = most_funded_city.sort_values(by='amount',ascending=False).head(10)

        most_funded_city['amount'] = round(most_funded_city['amount'],2)

        return most_funded_city
    
    def most_funded_startups_yoy(self):
        most_funded_startup_yoy = startup.groupby(['year','name'])['amount'].sum().sort_values(ascending=False).reset_index().drop_duplicates('year',keep='first').sort_values(by='year')
        most_funded_startup_yoy.rename(columns = {
            'year' : 'Year',
            'name':'StartUp Name',
            'amount':'Amount (In Crore Rs)'
        },inplace=True)

        return most_funded_startup_yoy
    
    
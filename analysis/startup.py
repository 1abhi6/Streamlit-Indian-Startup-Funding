from dataset import startup

class Startup:
    def __init__(self):
        self.startup = startup
    
    def list_of_startups(self):
        return list(startup['name'].sort_values().unique())[1:]

    def sector(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['vertical'].values[0]

    def subsector(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['subvertical'].values[0]

    def location(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['city'].values[0]

    def stage(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['type'].values[0]

    def investors(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['investors'].values[0]

    def investment_date(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['date'].values[0]
    
    def funding(self,startup_name):
        company = self.startup[self.startup['name'] == startup_name]
        return company.groupby('name')['amount'].sum().values[0]

    def similar_startups(self,startup_name):
        vertical = startup.loc[startup['name'] == startup_name, 'vertical'].values[0]

        temp_startups = startup.loc[startup['vertical'] == vertical, 'name'].unique()

        similar_startups = []
        for company in temp_startups:
            if company != startup_name:
                similar_startups.append(company)

        return similar_startups

import pandas as pd
import numpy as np

from dataset import startup

class Startup:
    def __init__(self):
        self.startup = startup

    def sector(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['vertical'].values[0]
    
    def subsector(self,startup_name);
        return self.startup[self.startup['name'] == startup_name]['subvertical'].values[0]
    
    def location(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['city'].values[0]
    
    def stage(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['type'].values[0]
    
    def list_of_investors(self,startup_name):
        return self.startup[self.startup['name'] == startup_name]['investors'].values[0]

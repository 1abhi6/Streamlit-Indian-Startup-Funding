import pandas as pd
import numpy as np

class Investor:
    def __init__(self):
        self.startup = pd.read_csv('dataset/startup_cleaned.csv')
    
    def investor_list(self):
        return sorted(set(self.startup['investors'].str.split(',').sum()))[2:]
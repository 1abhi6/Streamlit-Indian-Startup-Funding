import pandas as pd
import numpy as np

class Startup:
    def __init__(self):
        self.startup = pd.read_csv('dataset/startup_cleaned.csv')
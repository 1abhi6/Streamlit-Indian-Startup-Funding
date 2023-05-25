import pandas as pd
import numpy as np

from dataset import startup

class Startup:
    def __init__(self):
        self.startup = startup

    def sector(self):
        return self.startup[self.startup['name'] == 'Mamaearth']['vertical'].values[0]
    
    
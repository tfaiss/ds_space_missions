# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:46:00 2020

@author: Tobias Faiss
"""

import pandas as pd

path = "data/space_corrected.csv"
df = pd.read_csv(path)


## data cleaning activities
# separate location launch site and country
# divide detail in 'rocket' and 'satellite'
# change column 'rocket' to 'Costs in m USD'

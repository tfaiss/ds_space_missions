# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 18:46:00 2020

@author: Tobias Faiss
"""

## IMPORT LIBS
import pandas as pd


## LOAD DATASET
path = "data/space_corrected.csv"
df = pd.read_csv(path)


## FUNCTIONS


## RENAMING COLUMNS
# change column 'rocket' to 'Costs in m USD'
df.rename(columns = {' Rocket':'Costs (Mio. USD)'}, inplace=True)


## SEPARATE 'LOCATION' INTO 'LAUNCH SITE' AND 'COUNTRY'
# distill launch site from location and add it to dataframe
launch_site = df.Location.str.rsplit(',', 1)
launch_site = launch_site.tolist()
for i in launch_site:
    i.pop()
df['Site'] = launch_site


# distill country from location and add it to dataframe
country = df.Location.str.rsplit(',', -1)
country = country.tolist()
for i in country:
    del i[:-1]
df['Country'] = country


## SEPARATE 'DETAILS' INTO 'ROCKET' AND 'SATELLITE'
# distill rocket from details and add it to dataframe
rocket = df.Detail.str.rsplit(' | ', 1)
rocket = rocket.tolist()
for i in rocket:
    i.pop()  
df['Rocket'] = rocket

# distill satellite from details and add it to dataframe
satellite = df.Detail.str.rsplit(' | ', 1)
satellite = satellite.tolist()
for i in satellite:
    del i[:-1] 
df['Satellite'] = satellite


## DROP UNNECESSARY COLUMNS
# drop unnamed columns, location and detail since it has been replaced by new columns
df.drop(['Unnamed: 0', 'Unnamed: 0.1', 'Location', 'Detail'], axis=1, inplace=True)

## SAVE CLEANED DATA TO CSV
df.to_csv("data/space_corrected_cleaned.csv")


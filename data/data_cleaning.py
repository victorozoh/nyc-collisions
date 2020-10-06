#! /usr/bin/env python

import pandas as pd

# read data into a pandas dataframe
df = pd.read_csv('collisions.csv')

# Columns to drop
columns = ['LOCATION', 'VEHICLE TYPE CODE 1', 'VEHICLE TYPE CODE 2',
            'VEHICLE TYPE CODE 3', 'VEHICLE TYPE CODE 4', 'VEHICLE TYPE CODE 5']
df.drop(columns, inplace=True, axis=1)

# drop rows with missing zipcode data
df = df[ df['ZIP CODE'].notna() ]

# drop rows with missing latitude data
# This coincidentally takes care of rows with missing longitude data
df = df[ df['LATITUDE'].notna() ]

# rename columns for easier handling
rename_columns = {'CRASH DATE' : 'crash_date',
                    'CRASH TIME' : 'crash_time',
                    'BOROUGH' : 'borough',
                    'ZIP CODE' : 'zip_code',
                    'LATITUDE' : 'latitude',
                    'LONGITUDE': 'longitude',
                    'ON STREET NAME' : 'on_street_name',
                    'CROSS STREET NAME' : 'cross_street_name',
                    'OFF STREET NAME' : 'off_street_name',
                    'NUMBER OF PERSONS INJURED' : 'num_persons_injured',
                    'NUMBER OF PERSONS KILLED' : 'num_persons_killed',
                    'NUMBER OF PEDESTRIANS INJURED' : 'num_pedestrians_injured',
                    'NUMBER OF PEDESTRIANS KILLED' : 'num_pedestrians_killed',
                    'NUMBER OF CYCLIST INJURED' : 'num_cyclist_injured',
                    'NUMBER OF CYCLIST KILLED' : 'num_cyclist_killed',
                    'NUMBER OF MOTORIST INJURED' : 'num_motorist_injured',
                    'NUMBER OF MOTORIST KILLED' : 'num_motorist_killed',
                    'CONTRIBUTING FACTOR VEHICLE 1' : 'contributing_factor_vehicle_1',
                    'CONTRIBUTING FACTOR VEHICLE 2' : 'contributing_factor_vehicle_2',
                    'CONTRIBUTING FACTOR VEHICLE 3' : 'contributing_factor_vehicle_3',
                    'CONTRIBUTING FACTOR VEHICLE 4' : 'contributing_factor_vehicle_4',
                    'CONTRIBUTING FACTOR VEHICLE 5' : 'contributing_factor_vehicle_5',
                    'COLLISION_ID' : 'collision_id'
                    }
df.rename(columns=rename_columns, inplace=True)

# displays the columns with missing values
#df.isnull().sum()
# fill in missing values with 'NA'
df.on_street_name.fillna(value='NA', inplace=True)
df.cross_street_name.fillna(value='NA', inplace=True)
df.off_street_name.fillna(value='NA', inplace=True)
df.contributing_factor_vehicle_1.fillna(value='NA', inplace=True)
df.contributing_factor_vehicle_2.fillna(value='NA', inplace=True)
df.contributing_factor_vehicle_3.fillna(value='NA', inplace=True)
df.contributing_factor_vehicle_4.fillna(value='NA', inplace=True)
df.contributing_factor_vehicle_5.fillna(value='NA', inplace=True)

df.num_persons_injured.fillna(0, inplace=True)
df.num_persons_killed.fillna(0, inplace=True)

# convert num_persons_injured and num_persons_killed column from float to int
df['num_persons_injured'] = df['num_persons_injured'].astype(int)
df['num_persons_killed'] = df['num_persons_killed'].astype(int)

# convert date column to pandas datetime object
df['crash_date'] = pd.to_datetime(df['crash_date'])

# convert dataframe to csv and save
df.to_csv('cleaned_collisions.csv',  index=False)

print("data cleaning complete!")

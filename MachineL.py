import pandas as pd
import os
import sys, csv, glob
import uuid
import datetime
import matplotlib.pyplot as plt

# read data from the source file

df = pd.read_csv("/Users/shona/Downloads/2008_out.csv")

#df = df.convert_objects(convert_numeric=True)

# Adding UUID and Time stamp to the sample dataset

df['uuid'] = [uuid.uuid4() for x in range(len(df))]
df['Timestamp'] = [datetime.datetime.now() for x in range(len(df))]

# replace all the empty strings
df.replace(['nan', 'None'], '')

# write back to the staging file
#df.to_csv("/Users/shona/Downloads/2008_out.csv")

# checking which Counts for each Flight Num
#print(df.groupby("FlightNum").size().reset_index(name='Counts'))

#Which flight has max delay across operations

aggregations = {
    'ArrDelay':{"ArrDelayMean": "mean"}}
    #"ActualElapsedTime":['sum']

#Which carrier performs better?
#df = df.groupby(['FlightNum']).agg(aggregations)

#When is the best time of day/day of week/time of year to fly to minimise delays?
df = df.groupby(['Year','Month','DayofMonth','DayOfWeek']).agg(aggregations)

#df=df.columns.droplevel(0)

df.sort_index(axis=0,level=None,ascending=False)
#check if object is dataframe or not
print(isinstance(df,pd.DataFrame))

print(df.head)

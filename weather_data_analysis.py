import pandas as pd
mdata = pd.read_csv("C:/Users/Fola/Desktop/TOBI/CODES/weather analysis/1. Weather Data.csv")

1. Shape
mdata.shape

2. Data types
mdata.dtypes

3. Unique
mdata['Weather'].unique()

4. Count
mdata.count()

5. Value counts
mdata['Weather'].value_counts()

6.information
mdata.info

7.Describe
mdata.describe()

8.Head
mdata.head()

9.Index
mdata.index

10.Columns
mdata.columns

# To check if there are null values and drop them
print(mdata.isnull().sum())
mdata.dropna() #drop any row with NaN
mdata.dropna(axis=1) #drop any column with NaN

# To find unique instances of weather types
weather=mdata['Weather'].value_counts()
mdataweather=pd.DataFrame(weather)
mdataweather = mdataweather.reset_index()
mdataweather.columns = ['Weather', 'Frequency'] # change column names
print(mdataweather )

# To rename column named 'Weather' to Weather Condition'
a = mdata.rename(columns = {'Weather' : 'Weather_Condition'}, inplace=False)
print(a)

# To find all records from data of when the weather was exactly clear
print(mdata[mdata['Weather'] == 'Clear'])

# To find the mean temperature, wind speed and visibility
print(mdata['Temp_C'].mean())
print(mdata['Wind Speed_km/h'].mean())
print(mdata['Visibility_km'].mean())

# To find the variance of pressure
print(mdata['Press_kPa'].var())

# To find the days on which wind speed was less than or equal to 30 km/hr and temperature was greater than 0 C
windspeed=mdata[(mdata['Wind Speed_km/h'] <=30) & (mdata['Temp_C']>0)]
print(windspeed['Date/Time'])
print(windspeed.shape)

# To find the date and temperatures for all instances when snow was recorded
snow=mdata[mdata['Weather'] == 'Snow']
print(snow.loc[:, ['Date/Time', 'Temp_C']])

import matplotlib.pyplot as plt
import numpy as np
#matplotlib inline

# To display a graph of variation of temperature with respect to time
graph=mdata[['Temp_C', 'Date/Time']]
print(graph.plot(x='Date/Time', y='Temp_C',figsize=(10,7) ))

# To display a pie chart of percentages of weather conditions
#pie chart
keep=mdataweather[mdataweather['Frequency']>20]
print(keep)
keep.plot.pie(y='Frequency',autopct='%1.1f%%', shadow=False, figsize=(12,9))
plt.title("Weather Conditions")
plt.show()

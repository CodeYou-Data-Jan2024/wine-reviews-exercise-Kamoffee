# # add your code here
# import pandas as pd

# # Read the CSV file

# data_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# # Calculate count of reviews and average points for each country
# counts = data_reviews.groupby('country').size()
# country_points_average = data_reviews.groupby('country')['points'].mean().round(1)

# # Create the DataFrame
# datas = pd.DataFrame({
#     'country': counts.index,
#     'count': counts.values  ,
#     'points': country_points_average.values})
    

# # Set index as country
# datas.set_index('country', inplace=True)

# # Sort values by count and points descending
# datas.to_csv('data/reviews-per-country.csv', sep='|', encoding='utf-8')

import pandas as pd

# Read the CSV file
data_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

# Creating the coulumns we need grouping them by country
country_points_average = data_reviews.groupby('country').agg({'country': 'count', 'points': 'mean'}).round(1)

# Renaming the column country and reseting the index to country
datas = country_points_average.rename(columns={'country': 'count'}).reset_index()

# Creating the CSV file
datas.to_csv('data/reviews-per-country.csv', index=False)

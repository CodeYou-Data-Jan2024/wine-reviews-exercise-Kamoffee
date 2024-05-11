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
# sorting_data = datas.sort_values(by=['count'], ascending=False)
# sorting_data.to_csv('data/reviews-per-country.csv', sep='|', encoding='utf-8')

import pandas as pd
df_wine_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', compression='zip')

df_wine_by_countries_points = df_wine_reviews.groupby('country').agg({'country':'count', 'points': 'mean'}).round(1)
df_updated = df_wine_by_countries_points.rename(columns={'country':'count'}).reset_index()
df_updated.to_csv('data/reviews-per-country.csv', index=False)

# add your code here
import pandas as pd

# Read the CSV file

data_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Calculate count of reviews and average points for each country
counts = data_reviews.groupby('country').size()
country_points_average = data_reviews.groupby('country')['points'].mean()

# Create the DataFrame
datas = pd.DataFrame({
    'country': counts.index,
    'count': counts,
    'points': country_points_average.values.round(1)}).reset_index(drop=True)

# Set index as country
datas.set_index('country', inplace=True)

# Sort values by count and points descending
sorting_data = datas.sort_values(by=['count'], ascending=False)
# sorting_data.to_csv('data/reviews-per-country.csv', sep='|', encoding='utf-8')

output_data = pd.concat([sorting_data.head(5), sorting_data.tail(5)])
output_data.to_csv('data/reviews-per-country.csv', sep='|', encoding='utf-8')



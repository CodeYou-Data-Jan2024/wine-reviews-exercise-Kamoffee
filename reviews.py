# add your code here
import pandas as pd

# Read the CSV file
data_reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip')

# Calculate count of reviews and average points for each country
counts = data_reviews.groupby('country').size()
country_points_average = data_reviews.groupby('country')['points'].mean()

# Create the DataFrame
datas = pd.DataFrame({
    'count': counts,
    'points': country_points_average.values.round(1)}).reset_index()

# Set index as country
datas.set_index('country', inplace=True)

# Sort values by count and points descending
sorting_data = datas.sort_values(by=['count', 'points'], ascending=False)

sorting_data.to_csv('data/reviews-per-country.csv', sep='|', encoding='utf-8')



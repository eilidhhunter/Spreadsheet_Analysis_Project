import csv
import statistics
import pandas as pd

#initialise totals
total_sales = 0

with open('data/shopping_trends.csv', 'r') as csv_file:
    spreadsheet = csv.DictReader(csv_file)

# creating lists for each data field in csv
    purchase_data = []
    gender_data = []
    age_data = []
    item_data = []
    location_data = []
    size_data = []
    colour_data = []
    season_data = []
    shipping_type_data = []
    rating_data = []
    subscription_data = []
    category_data = []

    for row in spreadsheet:
        purchase_amount = int(row['Purchase Amount (USD)'])
        age = int(row['Age'])
        gender = str(row['Gender'])
        item = str(row['Item Purchased'])
        category = str(row['Category'])
        location = str(row['Location'])
        size = str(row['Size'])
        colour = str(row['Color'])
        season = str(row['Season'])
        rating = float(row['Review Rating'])
        subscription = str(row['Subscription Status'])

        purchase_data.append(purchase_amount)
        age_data.append(age)
        gender_data.append(gender)
        item_data.append(item)
        category_data.append(category)
        location_data.append(location)
        size_data.append(size)
        colour_data.append(colour)
        season_data.append(season)
        rating_data.append(rating)
        subscription_data.append(subscription)

# Calculate review score average
average_score = statistics.mean(rating_data)
print(f'The average review rating is {average_score:.2f}') #rounds to 2 dp

# Calculate the % of orders per season
summer_count = season_data.count('Summer')
fall_count = season_data.count('Fall')
winter_count = season_data.count('Winter')
spring_count = season_data.count('Spring')

total_season_count = summer_count + fall_count + winter_count + spring_count
summer_percentage = (summer_count/total_season_count) * 100
fall_percentage = (fall_count/total_season_count) * 100
winter_percentage = (winter_count/total_season_count) * 100
spring_percentage = (spring_count/total_season_count) * 100

print(f'The percentages of customer orders in each season is as below: \n Summer: '
      f'{summer_percentage:.1f}% \n Fall: {fall_percentage:.1f}% '
      f'\n Winter: {winter_percentage:.1f}% \n Spring: {spring_percentage:.1f}%')

#extract highest purchase amount
highest_purchase=max(purchase_data)
print(f'The largest transaction value made by a customer was ${highest_purchase}')

total_sales = sum(purchase_data)
print(f'The total income from sales was: ${total_sales:.2f}')


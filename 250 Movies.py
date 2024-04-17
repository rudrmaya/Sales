import pandas as pd
import numpy as np

# Load the dataset
file_path = 'C:\Users\mayan\OneDrive\Desktop\Code First Girls\250 Movies.py'
data = pd.read_csv(file_path)

# Clean the 'budget' column by removing non-numeric characters and handling empty entries
data['budget_clean'] = data['budget'].replace('[^\d.]', '', regex=True)
data['budget_clean'] = data['budget_clean'].replace('', np.nan, regex=True).astype(float)

# Calculate average IMDb rating
average_rating = data['rating'].mean()

# Find the earliest and latest release years
earliest_year = data['year'].min()
latest_year = data['year'].max()

# Calculate the average budget, excluding any NaN values
average_budget = data['budget_clean'].mean()

# Print the results
print("Average IMDb Rating:", average_rating)
print("Earliest Year of Release:", earliest_year)
print("Latest Year of Release:", latest_year)
print("Average Budget:", average_budget)

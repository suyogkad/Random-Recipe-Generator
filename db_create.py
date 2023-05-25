import pandas as pd
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('recipes.db')

# Read the CSV file into a DataFrame
df = pd.read_csv('Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

# Write the data to a table in the database
df.to_sql('recipes', conn, if_exists='replace', index=False)

conn.close()
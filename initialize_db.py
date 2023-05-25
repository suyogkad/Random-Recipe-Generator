import sqlite3
import pandas as pd

# Read the CSV data
data = pd.read_csv('Food Ingredients and Recipe Dataset with Image Name Mapping.csv')

# Create a connection to the SQLite database
# If the database does not exist, it will be created
conn = sqlite3.connect('recipes.db')

# Write the data to a SQLite table
data.to_sql('recipes', conn, if_exists='replace', index=False)

# Commit the transaction and close the connection
conn.commit()
conn.close()
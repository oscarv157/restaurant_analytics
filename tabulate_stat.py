import pandas as pd
from tabulate import tabulate

"""This is just to check whats being stored in the cleaned data, output in a tabulate form"""
input_folder = "combined_datafiles/combined_data.csv"

df = pd.read_csv(input_folder)

player_table  = tabulate(df, headers="keys",tablefmt='pretty', showindex=False)

print(player_table)
print(df.info())


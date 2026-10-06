import pandas as pd
from tabulate import tabulate

"""This is just to check whats being stored in the cleaned data, output in a tabulate form"""

input_folder = "clean_data_files/clean_data.csv"

df = pd.read_csv(input_folder)
# df = df[df['item'].str.contains('rueda', case = False,na=False)]

menu_table  = tabulate(df, headers="keys",tablefmt='pretty', showindex=False)
# summary = df[df['item'].str.contains('', case = False,na=False)]
# waza = tabulate(summary, headers="keys",tablefmt='pretty', showindex=False)
# # print(df[df["item"] == "Rinconcito Breakfast"])
print(menu_table)
# print(df.info())
# print(waza)
# print(len(summary))

print("Rows:", len(df))
print("Total quantity sold:", df["quantity"].sum())
print("Unique items:", df["item"].nunique())
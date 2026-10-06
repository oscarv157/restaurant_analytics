# import pandas as pd
# from tabulate import tabulate
# import re
# from pathlib import Path
# from rapidfuzz import process, fuzz
#
#
# # this was to print out all files in the directory
# # base_dir = Path("restaurant_raw_data/")
# # for file in base_dir.iterdir():
# #     if file.is_file():
# #         print(file)
#
# #this is to test the code to find any slightly misspelled words
# input_file = "clean_data.csv"
#
# df = pd.read_csv(input_file)
#
# unique_names = df['item'].unique().tolist()
# possible_dups = []
#
# for i in unique_names:
#     # print(i)
#     top_matches = process.extract(i, unique_names, scorer=fuzz.ratio, limit=3)
#     # possible_dups.append(top_matches)
#     for match_name, score, _ in top_matches:
#         if match_name != i and score >= 80: #change to 89.65 w/ some exceptions
#             possible_dups.append((i, match_name, score))
#
#
# # for k in possible_dups:
# #     print(k)
#
# dupli_name = pd.DataFrame(possible_dups, columns=["name 1", "name 2", "score"])
# dupli_name = dupli_name.sort_values('score', ascending=False)
# # print(dupli_name)
#
# # with pd.option_context('display.max_columns', None, 'display.max_rows', None):
# #     print(dupli_name)
#
# spell_fix = {}
# seen_pair = set()
# rows_to_review = []
#
# for _, row in dupli_name.iterrows():
#     pair = tuple(sorted([row['name 1'], row['name 2']]))
#     # print(f"@@",row)
#     if pair not in seen_pair:
#         seen_pair.add(pair)
#         rows_to_review.append(row)
#         # print(pair)
#
# for row in rows_to_review:
#     name1 = row['name 1']
#     name2 = row['name 2']
#
#     print(f"{name1} <---> {name2}")
#     print("Pick correct spelling or discard both:\n")
#     response = input(f"1. for {name1} 2. for {name2} 3.discard both")
#
#     if response == 1:
#         spell_fix
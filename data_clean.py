import pandas as pd
from pathlib import Path
from rapidfuzz import process, fuzz
import json

"""This file will clean up the csv file with the combined restaurant data """

input_file = "combined_datafiles/combined_data.csv"
spell_file = "clean_data_files/spell_fix.json"

output_file = "clean_data_files/clean_data.csv"
file_path = Path(output_file)
file_path.parent.mkdir(parents=True, exist_ok=True)
file_path.touch(exist_ok=True)

df = pd.read_csv(input_file)
# print(df.head())
# print(df['item'])
# print(df['item'].nunique())

print("***************")

def name_clean(df):
    df['item'] = (df['item'] #this is fixing the item names to make them more legible
                  .str.title()
                  .str.lstrip("-.")
                  .str.rstrip(".,-")
                  .str.strip())
    # print(df['item'])
    print("Items legibility check")
    return df

name_clean(df)
# print(df)
def spell_check(df):
    """This checks for any names that are similarly spelled. Some of these are misspelt,
        and the correct/better spelling is picked."""
    unique_names = df['item'].unique().tolist()
    possible_dups = []
    #This is checking for
    for i in unique_names:
        # print(i)
        top_matches = process.extract(i, unique_names, scorer=fuzz.ratio, limit=3)
        # possible_dups.append(top_matches)
        for match_name, score, _ in top_matches:
            if match_name != i and score >= 89.65:  # change to 89.65 w/ some exceptions. was at 80
                possible_dups.append((i, match_name, score))

    # for k in possible_dups:
    #     print(k)

    dupli_name = pd.DataFrame(possible_dups, columns=["name 1", "name 2", "score"])
    dupli_name = dupli_name.sort_values('score', ascending=False)
    # print(dupli_name)

    # with pd.option_context('display.max_columns', None, 'display.max_rows', None):
    #     print(dupli_name)

    # return df #OR send fix to csv? OR return dupli_name
    print("Spell Check complete")
    return dupli_name

duple_list = spell_check(df)

def spelling_list(dupli_name):
    """This function takes the dataframe of the spell_check names and lets user pick the correct spelling"""
    spell_fix = {}
    seen_pair = set()
    rows_to_review = []
    count = 1

    for _, row in dupli_name.iterrows():
        pair = tuple(sorted([row['name 1'], row['name 2']]))
        # print(f"@@",row)
        if pair not in seen_pair:
            seen_pair.add(pair)
            rows_to_review.append(row)
            # print(pair)

    for row in rows_to_review:
        name1 = row['name 1']
        name2 = row['name 2']

        # print(f"{name1} <---> {name2}")
        print(f"{count} / {len(rows_to_review)}")
        print("Pick correct spelling or discard both:")
        response = input(f"1.For {name1} 2.For {name2} 3. Any key to discard both\n")

        if response == '1':
            spell_fix[name2] = name1
        if response == '2':
            spell_fix[name1] = name2
        count+= 1

    # print("##########")
    # print(spell_fix)
    with open(spell_file, "w") as file:
        json.dump(spell_fix, file, indent=3)

#spelling_list(duple_list) #dictionary already has the list to fix

def spell_adjust():
    """This replaces the misspelt word for the proper one according to the menu"""
    with open(spell_file, "r") as file:
        data = json.load(file)
    # print(data)
    df['item'] = df['item'].replace(data)
    # print(df['item'].nunique())
    print("Misspelt items fixed")

spell_adjust()

comb_df = df.groupby(['week_start','week_end','hour','item'],as_index=False).agg({
    'quantity': 'sum',
    'price': 'sum'
}) #combining the repeated now fixed repeated item names
print("Repeated items merged")

comb_df = comb_df[~comb_df['item'].str.contains('==', na=False)] ##removing the == filler items
comb_df = comb_df[~comb_df['item'].str.contains('Cant', na=False)]
comb_df = comb_df[~comb_df['item'].str.contains('to go', case = False, na=False)]
comb_df = comb_df[~comb_df['item'].str.contains('mesa', case = False, na=False)]
comb_df = comb_df[~comb_df['item'].str.contains('Resumen De La Hora', case = False, na=False)]
print("Filler items removed")


# df.to_csv(output_file,index = False)

comb_df.to_csv(output_file,index = True)


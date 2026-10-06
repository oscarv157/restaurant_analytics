import pandas as pd
from tabulate import tabulate
import re
from pathlib import Path

"""This file is combining the data from the xls/text files with the restaurant data into a csv file"""

base_dir = Path("restaurant_raw_data/")
final_dir = Path("combined_datafiles/")
all_df = []

for file in base_dir.iterdir():
    input_file = file
    #input_file = "restaurant_raw_data/Informe de ventas por hora 07-20 a 07-26.xls",""
    output_file = final_dir
    data = []
    current_hour = None

    with open(input_file, "r", encoding="latin1") as file:
        for i, line in enumerate(file, 1):
            line = line.strip()
            # print(f"{i} X {line}")

            #This is looking for the start dates and end dates as de YYYY/MM/DD a YYYY/MM/DD
            date_set = re.search(r"de\s+(\d+/\d+/\d+)\s+a\s+(\d+/\d+/\d+)",line)
            if date_set:
                week_start = pd.to_datetime(date_set.group(1))
                week_end = pd.to_datetime(date_set.group(2))
                print(week_start)
                print(week_end)
                continue

            #This is grabbing the time by searching lines that contain >>> 00:00:00 a 00:00:00<<< ~format
            hour_set = re.search(r">>> de\s+(.+?) a\s+(.+?) <<<",line)
            if hour_set:
                current_hour = hour_set.group(1)
                # print(f"HII {current_hour}")

            if (not line
                    or line.startswith("NOMBRE DEL PLATILLO")
                    or line.startswith("--------------")
            ):
                continue

            part = line.split()
            # print(part)
            if len(part) >= 4 and current_hour is not None:
                # print(current_hour, part)
                try:
                    item = " ".join(part[:-3])
                    quantity = float(part[-1])
                    # print(quantity)
                    percent = float(part[-2].replace("%", ""))
                    # print(percent)
                    price = float(part[-3])
                    # print(price)
                    # print(f"CHECK, {item},{quantity}, {percent}, {price}")
                    """clean_name = item.title().lstrip("-.").rstrip(".,-").strip() #use this for data cleaning"""

                    data.append({
                        "week_start": week_start,
                        "week_end": week_end,
                        "hour": current_hour,
                        "item": item,
                        "quantity": quantity,
                        "percent": percent,
                        "price": price
                    })

                except ValueError:
                    continue

    df = pd.DataFrame(data)
    all_df.append(df)

combined_df = pd.concat(all_df, ignore_index=True)
# df = pd.read_csv(input_file,sep="\t",encoding="latin1")
# df = pd.DataFrame(data)
print(combined_df.head())
print(combined_df.shape)
# pretty_table  = tabulate(combined_df, headers="keys",tablefmt='pretty', showindex=False)
# print(pretty_table)
# print(df.isnull().sum)
combined_df.to_csv(final_dir / "combined_data.csv") #(final_dir / "combined_data.csv", index=False)

df.to_csv(final_dir,index = False)
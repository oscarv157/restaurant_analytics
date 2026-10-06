import pandas as pd
from dotenv import load_dotenv
import psycopg2
import os
from sqlalchemy import create_engine
load_dotenv()

"""This file is to send the data up to the database. 
    Sends the info into three tables: items, weeks, & sales"""

df = pd.read_csv("clean_data_files/clean_data.csv")

db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PSWD")
db_host = os.environ.get("DB_HOST") #in the future, may use AWS as cloud host

# try: #checking connection to db before moving on to using sql alchemy
#     conn = psycopg2.connect(
#         dbname = db_name,
#         user = db_user,
#         password = db_password,
#         host = db_host
#     )
#
#     print(f"Connected successfully")
#     conn.close()
#
# except Exception as error:
#     print(f"Unable to connect to database: {error}")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:5432/{db_name}")

with engine.connect() as connection: #this is for the database connection with sqlalchemy
    print(f"Connected engine")

def make_week(): #this is sending the week info to the database
    weeks_df = df[['week_start','week_end']].drop_duplicates()

    weeks_df.to_sql(
        name = 'weeks',
        con = engine,
        index = False,
        if_exists = "append",
    )
    print("Week info now in database")

make_week()

def make_item(): #this is sending the item info to the database
    items_df = df[["item"]].drop_duplicates()
    items_df = items_df.rename(columns={'item':'item_name'})
    # print(items_df)

    items_df.to_sql(
        name = 'items',
        con = engine,
        index = False,
        if_exists = 'append',
    )
    print("Item info now in database.")

make_item()

def sales_setup(df): #this is set up the foreign keys for the sales table
    week_db = pd.read_sql("SELECT week_id, week_start, week_end FROM weeks", engine)
    item_db = pd.read_sql("SELECT item_id, item_name FROM items", engine)
    # print(df.dtypes)
    #Changing the weeks from str to objects; this was causing issues in the creation of sales
    df["week_start"] = pd.to_datetime(df["week_start"]).dt.date
    df["week_end"] = pd.to_datetime(df["week_end"]).dt.date

    # print(week_db.dtypes)
    # print(item_db)
    df = df.merge(
        week_db,
        on=["week_start", "week_end"],
        how="left"
    )
    df = df.merge(
        item_db,
        left_on=["item"],
        right_on=["item_name"],
        how="left"
    )
    return df

df = sales_setup(df)


def make_sales():
    sales_df = df[["week_id", "item_id", "hour", "price", "quantity"]]

    sales_df = sales_df.rename(columns={"price":"sales"})

    sales_df.to_sql(
        name = 'sales',
        con = engine,
        index = False,
        if_exists = 'append'
    )
    print("Sale info now in database")

# print(df.columns)
make_sales()

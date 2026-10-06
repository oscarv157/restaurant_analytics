import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from pathlib import Path
import plotly.express as px

load_dotenv()

"""This file is to take in the data from the db and make stat analysis on it"""

db_name = os.environ.get("DB_NAME")
db_user = os.environ.get("DB_USER")
db_password = os.environ.get("DB_PSWD")
db_host = os.environ.get("DB_HOST")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:5432/{db_name}")

with engine.connect() as connection:
    print(f"Connected engine")

def weeks_in_file():
    with open("sql/available_weeks.sql") as file:
        query = file.read()

    df = pd.read_sql(query,engine)
    return df

def most_item_per_hour():
    with open("sql/most_sold_item_per_hour.sql","r") as file:
        query = file.read()

    df = pd.read_sql(query,engine)
    return df

# most_item_per_hour()

def hourly_ranking():
    with open("sql/hour_sales_ranked.sql", "r") as file:
        query = file.read()

    df = pd.read_sql(query,engine)
    # print(df)
    return df

# hourly_ranking()

def top_items_quantity():
    with open("sql/most_sold_items.sql", "r") as file:
        query = file.read()

    df = pd.read_sql(query,engine)
    # print(df)
    return df

# top_items_quantity()

def top_items_sale():
    with open("sql/top_items_sale", "r") as file:
        query = file.read()

    df = pd.read_sql(query, engine)
    #print(df)
    return df

# top_items_sale()

def weekly_sales():
    with open("sql/week_total_sale.sql", "r") as file:
        query = file.read()

    df = pd.read_sql(query, engine)
    # print(df)
    return df

# weekly_sales()

def top_weekly_items():
    with open("sql/top_weekly_item.sql", "r") as file:
        query = file.read()

    df = pd.read_sql(query, engine)
    # print(df)
    return df

# top_weekly_items()

def top_item_performance(var = 's.sales'): #var is either s.sales or s.quantity
    query = f"""WITH top_item AS (
        SELECT
            s.item_id
        FROM sales s
        GROUP BY s.item_id
        ORDER BY SUM({var}) DESC
        LIMIT 1
        )
    
        SELECT
            w.week_start,
            w.week_end,
            i.item_name,
            SUM(s.sales) AS total_sales,
            SUM(s.quantity) AS total_quantity
        FROM sales s
        JOIN weeks w
            ON s.week_id = w.week_id
        JOIN items i
            ON s.item_id = i.item_id
        JOIN top_item t
            ON s.item_id = t.item_id
        GROUP BY
            w.week_start,
            w.week_end,
            i.item_name
        ORDER BY
            w.week_start;"""

    df = pd.read_sql(query, engine)
    # print(df)
    return df

# top_item_performance()

def top_items_by_week(week_start=None):
    query = text("""
        SELECT
            i.item_name,
            SUM(s.sales) AS total_sale,
            SUM(s.quantity) AS total_quantity
        FROM sales s
        JOIN items i
            ON s.item_id = i.item_id
        JOIN weeks w
            ON s.week_id = w.week_id
        WHERE (
            CAST(:week_start AS DATE) IS NULL
            OR w.week_start = CAST(:week_start AS DATE)
        )
        GROUP BY i.item_name
        ORDER BY total_quantity DESC
        LIMIT 10;
    """)

    df = pd.read_sql_query(query, engine, params={"week_start": week_start})
    print(df)
    return df
top_items_by_week()
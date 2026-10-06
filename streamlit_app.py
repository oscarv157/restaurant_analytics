import pandas as pd
import streamlit as st
import plotly.express as px
import analysis
from translations_rest import translations_rest


st.title("Restaurant Analysis:")
st.subheader("Rinconcito Cubano Criollo")

date_range = analysis.weeks_in_file()
first_week = date_range.iloc[0, 0]
last_week = date_range.iloc[1, -1]

st.caption(f"{first_week:%m/%d/%Y} - {last_week:%m/%d/%Y}")

language = st.selectbox(
    "Language / Idioma",
    ["English", "Spanish"]
)
lang =  "en" if language == "English" else "es"
t = translations_rest[lang]

st.subheader(t["title"])
tab1, tab2 = st.tabs(["Homepage","Extra"])

with tab1: #first tab will display overall stats
    choices ={
        t["sales"]: "s.sales",
        t["quantity"]: "s.quantity",
    }
    selected = st.selectbox((t["by_view"]), choices)
    var = choices[selected]
    df = analysis.top_items_sale()
    df2 = analysis.top_item_performance(var)

    st.subheader(t["statistics"])
    st.markdown(f"### :green[:material/arrow_forward_ios: {t["top_item_sold"]}]: {df2.loc[0, 'item_name']}")
    st.markdown(f"### :blue[:material/arrow_forward_ios: {t["quantity"]}]: {(df2['total_quantity']).sum()}")
    st.markdown(f"### :violet[:material/arrow_forward_ios: {t["sales_generated"]}]: $ {(df2['total_sales']).sum()}")

    if var == "s.quantity":
        fig = px.bar(
            df2,
            x=df2['week_start'],
            y=df2['total_quantity'],
            title=""

        )
        fig.update_traces(
            hovertemplate=
            f"{t["week"]}" + ": %{x}<br>" +
            f"{t["quantity"]}: " + " %{y}<br>" +
            "<extra></extra>"
        )
    else:
        fig = px.bar(
            df2,
            x=df2['week_start'],
            y=df2['total_sales'],
            title=""
        )
        fig.update_traces(
            hovertemplate=
            f"{t["week"]}" + ": %{x}<br>" +
            f"{t["total_sales"]}: $" + " %{y}<br>" +
            "<extra></extra>"
        )

    st.plotly_chart(fig)
    st.dataframe(df2)


with tab2:
    df = analysis.most_item_per_hour()
    st.subheader("")
    fig = px.bar(
        df,
        title=t['hourly_sale_total'],
        x=df['hour'],
        y=df['total_quantity'],
        custom_data=['item_name']  # this is displayed when hovering over bar?)
    )

    fig.update_traces(
        hovertemplate=
        f"{t["hour"]}" + ": %{x}<br>" +
        f"{t["quantity"]}:" + " %{y}<br>" +
        f"{t["top_item_sold"]}" + ": %{customdata[0]}" +
        "<extra></extra>"
    )

    st.plotly_chart(fig)


    weeks_df = analysis.weeks_in_file()
    opt = t["all_week"]
    week_options = [t["all_week"]] + [
        f"{row.week_start} to {row.week_end}"
        for row in weeks_df.itertuples()
    ]

    selected_week = st.selectbox(t["select_week"], week_options)
    if selected_week == t["all_week"]:
        week_start = None
    else:
        week_index = week_options.index(selected_week) - 1
        week_start = weeks_df.iloc[week_index]["week_start"]

    df2 = analysis.top_items_by_week(week_start)
    fig = px.bar(
        df2,
        title=t['weekly_sale'],
        x=df2["total_quantity"],
        y=df2["item_name"],

    )
    fig.update_layout(yaxis = {"categoryorder": "total ascending"})
    st.plotly_chart(fig)

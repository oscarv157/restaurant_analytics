# Restaurant Sales Analytics Pipeline & Dashboard

An end-to-end data analytics project built for a local restaurant in Miami, Florida, to improve visibility into sales trends and menu item performance using Python, PostgreSQL, SQL, and Streamlit.

## Overview

While working as a restaurant manager, I noticed that the existing point-of-sale (POS) system provided limited visibility into sales trends, including top-selling menu items, weekly performance, and hourly product performance.

After discussing the idea with the restaurant's owners, I developed a data pipeline and interactive dashboard to transform raw POS reports into structured data and actionable visualizations.

## Project Features

- **ETL Pipeline:** Used Python and Pandas to extract, clean, and transform weekly POS sales reports.
- **Relational Database:** Designed a PostgreSQL database to organize sales data, menu items, and reporting periods.
- **SQL Analysis:** Developed queries to analyze sales trends, top-selling items, and product performance across weeks and hours.
- **Interactive Dashboard:** Built a Streamlit dashboard with Plotly visualizations for exploring sales trends and menu item performance.
- **Bilingual Interface:** Supported both English and Spanish.
- **Presentation:** Presented the completed dashboard to the restaurant owners.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and ETL |
| Pandas | Data cleaning and transformation |
| PostgreSQL | Relational data storage |
| SQL | Sales analysis and querying |
| Streamlit | Interactive dashboard |
| Plotly | Data visualization |

## Data Pipeline

POS Reports → Python/Pandas ETL → PostgreSQL Database → SQL Analysis → Streamlit Dashboard

1. **Extract:** Read weekly POS sales reports.
2. **Transform:** Cleaned and standardized menu item names, dates, hourly categories, and sales fields.
3. **Load:** Organized the processed data into PostgreSQL tables.
4. **Analyze:** Used SQL queries to examine sales trends and menu item performance.
5. **Visualize:** Presented the results through interactive charts and dashboard components.

## Key Metrics

The project processed data covering multiple reporting weeks, including:

- **18,000+** sales records
- **480+** unique menu items
- **7+ weeks** of POS reporting data

## Privacy Notice

The original POS reports and business sales data are private and are not included in this repository. Any publicly shared sample data or screenshots should use synthetic data to protect the restaurant's confidential information.

## Author

Developed as a project-based data analytics initiative, combining real-world business context with data engineering and visualization.

**Technologies:** Python, Pandas, PostgreSQL, SQL, Streamlit, Plotly

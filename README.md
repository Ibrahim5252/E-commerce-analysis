# 📊 E-Commerce Sales & Profitability Dashboard

An interactive business analytics dashboard built with **Streamlit** and **Pandas** to analyze retail performance, monitor core financial KPIs, and pinpoint margin leaks down to individual product SKUs.

---

## 📌 Overview

Raw transactional datasets often bury critical business drivers behind thousands of rows. This application transforms unorganized e-commerce retail data into an intuitive, filterable web application. It enables stakeholders to track revenue fluctuations, compare category performance across regions, and quickly isolate loss-making inventory.

---

## ✨ Key Features

- **Dynamic Multi-Criteria Filtering**: Filter global transaction data on the fly by **Region** (Central, East, South, West) and **Category** (Furniture, Office Supplies, Technology).
- **Core KPI Summary Cards**: Instant calculation of aggregate metrics based on active filter selections:
  - **Total Sales**
  - **Total Profit**
  - **Average Profit Margin**
- **Sales Over Time**: High-resolution timeline tracking macro trends, order spikes, and revenue volume across multiple years.
- **Category Profit Breakdown**: Bar chart visualizing net profit distributions across distinct merchandise departments.
- **Loss-Making Products Watchlist**: A dedicated table filtering down to underperforming and negative-margin products (`Profit < 0`) to assist inventory and pricing decisions.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Data Manipulation**: [Pandas](https://pandas.pydata.org/)
- **Dashboard Framework**: [Streamlit](https://streamlit.io/)
- **Visualization**: Matplotlib / Plotly
- **Data Source**: Retail Transaction Dataset (Kaggle)

---

## 📂 Project Structure

```text
├── data/
│   └── Superstore_sales_dataset.csv       # Raw dataset
├── src/
│   └── analysis.py
│   └── cleaning.py
│   └── visualization.py
├── app.py                        # Streamlit application code
└── README.md

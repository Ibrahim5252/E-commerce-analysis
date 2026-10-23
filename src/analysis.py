def category_profit(df):
    return df.groupby("category")["Profit"].sum().sort_values()

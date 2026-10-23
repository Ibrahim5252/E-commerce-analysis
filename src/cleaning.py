import pandas as pd

def load_and_clean_data(path):
    df = pd.read_csv(path)
    df.drop_duplicates(inplace=True)
    df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
    df['Profit Margin'] = df['Profit'] / df['Sales']
    df['Year'] = df['Order Date'].dt.year
    df['Month'] = df['Order Date'].dt.month
    #! dayfirst=True → fixes your current issue
    #!errors="coerce" → converts bad values to NaT instead of crashing
    return df

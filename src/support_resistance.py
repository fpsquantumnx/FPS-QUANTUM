import pandas as pd

def find_support_resistance(df: pd.DataFrame, lookback: int = 20):
    if len(df) < 2:
        return None, None
    window = df.tail(min(lookback, len(df)))
    support = window["Low"].min()
    resistance = window["High"].max()
    return support, resistance

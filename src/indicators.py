import pandas as pd

def add_indicators(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["SMA20"] = out["Close"].rolling(20).mean()
    out["SMA40"] = out["Close"].rolling(40).mean()

    middle = out["Close"].rolling(20).mean()
    std = out["Close"].rolling(20).std(ddof=0)

    out["BB_Middle"] = middle
    out["BB_Upper"] = middle + (2 * std)
    out["BB_Lower"] = middle - (2 * std)
    return out

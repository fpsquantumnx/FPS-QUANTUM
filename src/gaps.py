import pandas as pd

def detect_gaps(df: pd.DataFrame, min_gap_pct: float = 0.5) -> pd.DataFrame:
    if len(df) < 2:
        return pd.DataFrame(columns=["date", "type", "gap_pct"])

    prev_close = df["Close"].shift(1)
    gap_pct = ((df["Open"] - prev_close) / prev_close) * 100

    result = pd.DataFrame(index=df.index)
    result["gap_pct"] = gap_pct
    result["type"] = "none"
    result.loc[result["gap_pct"] >= min_gap_pct, "type"] = "gap_up"
    result.loc[result["gap_pct"] <= -min_gap_pct, "type"] = "gap_down"
    result = result[result["type"] != "none"].copy()
    result.insert(0, "date", result.index.astype(str))
    return result[["date", "type", "gap_pct"]]

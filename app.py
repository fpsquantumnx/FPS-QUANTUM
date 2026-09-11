import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.graph_objects as go

from src.indicators import add_indicators
from src.support_resistance import find_support_resistance
from src.gaps import detect_gaps

st.set_page_config(page_title="FPS QUANTUM", page_icon="📈", layout="wide")

st.title("FPS QUANTUM")
st.caption("Open-source quantitative analysis toolkit for stocks and options.")

with st.sidebar:
    st.header("Market input")
    ticker = st.text_input("Ticker", value="SPY").strip().upper()
    period = st.selectbox("Period", ["1mo", "3mo", "6mo", "1y", "2y"], index=2)
    interval = st.selectbox("Interval", ["1d", "1h", "30m", "15m"], index=0)
    run = st.button("Run analysis", type="primary", use_container_width=True)

@st.cache_data(ttl=900)
def load_data(symbol: str, period_: str, interval_: str) -> pd.DataFrame:
    data = yf.download(symbol, period=period_, interval=interval_, auto_adjust=False, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)
    data = data.dropna(how="all")
    return data

if run:
    if not ticker:
        st.warning("Enter a ticker.")
        st.stop()

    try:
        df = load_data(ticker, period, interval)
    except Exception as exc:
        st.error(f"Could not download data: {exc}")
        st.stop()

    if df.empty:
        st.error("No market data returned for that ticker/period.")
        st.stop()

    df = add_indicators(df)
    support, resistance = find_support_resistance(df)
    gaps = detect_gaps(df)

    latest = df.iloc[-1]
    trend = "Bullish" if latest["SMA20"] > latest["SMA40"] else "Bearish / neutral"

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Last close", f"{latest['Close']:.2f}")
    c2.metric("SMA20", f"{latest['SMA20']:.2f}")
    c3.metric("SMA40", f"{latest['SMA40']:.2f}")
    c4.metric("Trend PM20/PM40", trend)

    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index, open=df["Open"], high=df["High"], low=df["Low"], close=df["Close"],
        name="Price"
    ))
    fig.add_trace(go.Scatter(x=df.index, y=df["SMA20"], name="SMA20"))
    fig.add_trace(go.Scatter(x=df.index, y=df["SMA40"], name="SMA40"))
    fig.add_trace(go.Scatter(x=df.index, y=df["BB_Upper"], name="Bollinger Upper", line=dict(dash="dot")))
    fig.add_trace(go.Scatter(x=df.index, y=df["BB_Middle"], name="Bollinger Middle", line=dict(dash="dot")))
    fig.add_trace(go.Scatter(x=df.index, y=df["BB_Lower"], name="Bollinger Lower", line=dict(dash="dot")))

    if support is not None:
        fig.add_hline(y=support, line_dash="dash", annotation_text="Support")
    if resistance is not None:
        fig.add_hline(y=resistance, line_dash="dash", annotation_text="Resistance")

    fig.update_layout(
        title=f"{ticker} — price, PM20/PM40 and Bollinger Bands",
        xaxis_rangeslider_visible=False,
        height=650
    )
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Volume")
    vol = go.Figure(go.Bar(x=df.index, y=df["Volume"], name="Volume"))
    vol.update_layout(height=280)
    st.plotly_chart(vol, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.subheader("Support / resistance")
        st.write({
            "support": None if support is None else round(float(support), 2),
            "resistance": None if resistance is None else round(float(resistance), 2),
        })

    with right:
        st.subheader("Recent gaps")
        if gaps.empty:
            st.write("No gaps detected with the current simple rule.")
        else:
            st.dataframe(gaps.tail(10), use_container_width=True)

    st.subheader("Latest indicator values")
    cols = ["Open", "High", "Low", "Close", "Volume", "SMA20", "SMA40",
            "BB_Middle", "BB_Upper", "BB_Lower"]
    st.dataframe(df[cols].tail(20), use_container_width=True)

    st.info(
        "FPS QUANTUM is an analytical/research tool. It does not provide individualized financial advice "
        "or guarantee future market performance."
    )
else:
    st.write(
        "Choose a ticker and click **Run analysis**. "
        "The first public version includes PM20/PM40, Bollinger Bands, volume, "
        "basic support/resistance and simple gap detection."
    )

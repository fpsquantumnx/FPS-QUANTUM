# FPS QUANTUM

**FPS QUANTUM** is an early-stage open-source quantitative market-analysis toolkit focused on stocks and options.

The project is being built to combine several forms of market evidence in one reproducible workflow instead of treating indicators in isolation.

## Current V0.1 features

- Market data retrieval through `yfinance`
- Candlestick chart
- 20-period simple moving average (SMA20 / PM20)
- 40-period simple moving average (SMA40 / PM40)
- Classical Bollinger Bands: 20-period SMA, 2 standard deviations, closing price
- Volume visualization
- Basic 20-bar support and resistance
- Simple gap-up / gap-down detection
- Streamlit user interface

## Project direction

Planned modules include:

- richer price-action and candle-pattern analysis
- floor / ceiling / channel detection
- volatility analytics
- options-chain analysis
- spot-to-strike distance filters
- expiration-window analysis
- event-aware research
- signal scoring from multiple independent factors
- reproducible research tables and reports

## Installation

```bash
git clone https://github.com/fpsquantummx/FPS-QUANTUM.git
cd FPS-QUANTUM
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Methodology

The current project intentionally avoids treating a single indicator as a prediction engine. Signals are intended to be interpreted together with trend, volatility, volume, price structure and, in later versions, options-market context.

See [`docs/methodology.md`](docs/methodology.md).

## Roadmap

See [`docs/roadmap.md`](docs/roadmap.md).

## Status

This repository is under active early-stage development. Contributions, issues and reproducible test cases are welcome.

## License

MIT License.

## Disclaimer

FPS QUANTUM is provided for education, research and analytical experimentation. It is not individualized investment advice and does not guarantee future results.

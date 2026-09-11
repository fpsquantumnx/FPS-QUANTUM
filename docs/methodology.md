# FPS QUANTUM — Methodology Notes

FPS QUANTUM is designed around a multi-factor approach.

## 1. Trend

The initial trend rule compares:

- PM20 / SMA20
- PM40 / SMA40

A simple bullish condition is PM20 > PM40. This condition is not treated as sufficient by itself.

## 2. Bollinger Bands

The initial configuration uses:

- 20 periods
- simple moving average
- 2 standard deviations
- closing price

The upper and lower bands measure price relative to recent volatility. Touching a band is not automatically interpreted as a reversal signal.

## 3. Volume

Volume is displayed alongside price so that price moves can be assessed in the context of participation.

## 4. Price structure

The first version uses a basic rolling-window approximation of support and resistance. Future versions will add pivot-based and channel-based structure detection.

## 5. Gaps

The initial implementation detects gaps between the prior close and the current open using a configurable percentage threshold.

## 6. Options layer — planned

The options layer will progressively add:

- calls and puts
- strike selection
- spot-to-strike distance
- expiration analysis
- volatility context
- scenario tracking

## Design principle

No single indicator is assumed to predict the market reliably on its own. FPS QUANTUM aims to combine independent evidence into a transparent, inspectable research workflow.

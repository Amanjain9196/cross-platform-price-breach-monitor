# Cross-Platform Price Breach Monitor

**Repository description:** Automated marketplace price-monitoring system that flags SKU-level breaches across platforms and prioritizes corrective action.

> Synthetic portfolio project only. No real employer prices, account identifiers, credentials or confidential marketplace data are included.

## Problem
Brands often sell the same SKU across multiple marketplaces. A price drop on one platform can trigger channel conflict, margin erosion or price parity issues before teams notice it manually.

## Solution
This project compares observed marketplace prices against a configured floor price and expected reference price, calculates breach severity and outputs a prioritized action queue.

## Architecture
```text
Platform feeds/scrapers -> SKU normalization -> Price rules -> Breach engine -> Alerts/report
```

## Features
- Cross-platform SKU matching
- Floor-price breach detection
- Breach amount and severity scoring
- Platform/SKU summary
- Synthetic data + auditable rules

## Run
```bash
pip install -r requirements.txt
python app.py
```

## Portfolio signal
Demonstrates monitoring automation, anomaly detection, data normalization and operational alerting across commerce platforms.

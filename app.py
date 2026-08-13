import pandas as pd
from pathlib import Path

DATA = Path('data/prices.csv')


def analyze_prices(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out['breach_amount'] = (out['floor_price'] - out['observed_price']).clip(lower=0)
    out['breach_pct'] = (out['breach_amount'] / out['floor_price']).fillna(0)
    out['is_breach'] = out['breach_amount'] > 0
    out['severity'] = pd.cut(
        out['breach_pct'],
        bins=[-0.001, 0, 0.05, 0.10, 1.0],
        labels=['OK', 'Low', 'Medium', 'High']
    )
    return out.sort_values(['is_breach','breach_pct'], ascending=[False,False])


def main():
    df = pd.read_csv(DATA)
    report = analyze_prices(df)
    print(report.to_string(index=False))
    breached = report[report['is_breach']]
    print(f"\nBreaches detected: {len(breached)} / {len(report)} observations")

if __name__ == '__main__':
    main()

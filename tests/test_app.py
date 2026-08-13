import pandas as pd
from app import analyze_prices


def test_detects_floor_breach():
    df = pd.DataFrame([{'sku':'X','platform':'P','floor_price':100,'reference_price':110,'observed_price':90}])
    out = analyze_prices(df)
    assert bool(out.iloc[0]['is_breach']) is True
    assert out.iloc[0]['breach_amount'] == 10


def test_no_breach_at_floor():
    df = pd.DataFrame([{'sku':'X','platform':'P','floor_price':100,'reference_price':110,'observed_price':100}])
    out = analyze_prices(df)
    assert bool(out.iloc[0]['is_breach']) is False

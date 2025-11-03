import yfinance as yf
from datetime import date
from datetime import datetime

def extract_data(start, end, stock):
    SENSEX = yf.Ticker(stock)
    if end == datetime.now().year:
        end = date.today()
        try:
            sensex_data = SENSEX.history(start=f"{start}-01-01", end=end)
            if sensex_data.empty:
                print(f"No data found for the period {start} to {end}.")
                sensex_data = None
        except Exception as e:
            print(f"Error fetching data for {start} to {end}: {e}")
            sensex_data = None
    else:
        try:
            sensex_data = SENSEX.history(start=f"{start}-01-01", end=f"{end}-12-31")
            if sensex_data.empty:
                print(f"No data found for the period {start} to {end}.")
                sensex_data = None
        except Exception as e:
            print(f"Error fetching data for {start} to {end}: {e}")
            sensex_data = None
    return sensex_data
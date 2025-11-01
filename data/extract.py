import yfinance as yf
from datetime import date
from datetime import datetime
SENSEX = yf.Ticker("^BSESN")
def extract_data(start, end):
    if end == datetime.now().year:
        end = date.today()
        try:
            SENSEXDATA = SENSEX.history(start=f"{start}-01-01", end=end)
        except Exception as e:
            print(f"Error fetching data for {start} to {end}: {e}")
            SENSEXDATA = None
        finally:
            pass
    else:
        try:
            SENSEXDATA = SENSEX.history(start=f"{start}-01-01", end=f"{end}-12-31")
        except Exception as e:
            print(f"Error fetching data for {start} to {end}: {e}")
            SENSEXDATA = None
        finally:
            pass
    return SENSEXDATA
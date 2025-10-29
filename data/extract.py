import yfinance as yf
from datetime import date
from datetime import datetime
SENSEX = yf.Ticker("^BSESN")
def extract_data(start, end):
    if end == datetime.now().year:
        end = date.today()
        SENSEXDATA = SENSEX.history(start=f"{start}-01-01", end=end)
    else:
        SENSEXDATA = SENSEX.history(start=f"{start}-01-01", end=f"{end}-12-31")
    return SENSEXDATA




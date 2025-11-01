from extract import extract_data
import time

#Define start and end years
start_year = 2000
end_year = 2025
interval = "1h"
#Extract Sensex data for the defined period
#Note that to avoid hitting API rate limits, we will extract data 2 years at a time and add delays between calls
for year in range(start_year, end_year + 1):
    start = year
    end = min(year, end_year)
    print(f"Extracting data from {start} to {end}...")
    sensex_data = extract_data(start, end, interval)

    #Store the data in a CSV file
    sensex_data.to_csv(f"sensex_data_{interval}_{start}_to_{end}.csv")

    time.sleep(10)
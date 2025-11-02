from extract import extract_data
import time

#Define start and end years
start_year = 2000
end_year = 2025
#Extract Sensex data for the defined period
#Note that to avoid hitting API rate limits, we will extract data 5 years at a time and add delays between calls
for year in range(start_year, end_year + 1, 5):
    start = year
    end = min(year + 4, end_year)
    print(f"Extracting data from {start} to {end}...")
    sensex_data = extract_data(start, end)

    #Store the data in a CSV file
    sensex_data.to_csv(f"sensex_data_try_{start}_to_{end}.csv")

    time.sleep(10)
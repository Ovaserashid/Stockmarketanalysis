import pandas as pd

'''Merge multiple CSV files containing stock market data into a single csv file.
   So that the transformation of the data is applied to all the data at once.
   
   The CSV files are assumed to be named in the format 'sensex_data_{start_year}_to_{end_year}.csv
   where start_year and end_year are in increments of 5 years from 2000 to 2025.'''


#Define years range
start_year = 2000
end_year = 2024

'''Make loop from start_year to end_year and read each CSV file, appending the data to a list then 
   concatenate all dataframes in the list into a single dataframe and save to a new CSV file.'''

data_list = []

#Loop through the years in increments of 5
for year in range(start_year, end_year + 1, 5):
    start = year
    end = min(year + 4, end_year)
    file_name = f"sensex_data_INFY.NS_{start}_to_{end}.csv"
    try:
        data = pd.read_csv(file_name, index_col=0, parse_dates=True)
        data_list.append(data)
    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping...")
    except Exception as e:
        print(f"Error reading {file_name}: {e}")

#Concatenate all dataframes in the list
if data_list:
    merged_data = pd.concat(data_list)

    #Save the merged data to a new CSV file
    merged_data.to_csv(f"sensex_data_INFY_{start_year}_to_{end_year}.csv")
    print(f"Merged data saved to sensex_data_{start_year}_to_{end_year}.csv")


"""
Process a CSV file on 2020 Happiness ratings by country to analyze the `Ladder score` column and save statistics.
"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import pathlib
import csv
import statistics
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

# TODO: Replace with the names of your folders
FETCHED_DATA_DIR: str = "sydney_project_data"
PROCESSED_DIR: str = "sydney_project_processed"

#####################################
# Define Functions
#####################################

# TODO: Add or replace this with a function that reads and processes your CSV file

def analyze_usd_rate(file_path: pathlib.Path) -> dict:
    """Analyze the USD column to calculate min, max, mean, and stdev."""
    try:
        # initialize an empty list to store the scores
        rate_list = []
        with file_path.open('r') as file:
            # csv.DictReader() methods to read into a DictReader so we can access named columns in the csv file
            dict_reader = csv.DictReader(file)  
            for row in dict_reader:
                try:
                    rate = float(row["USD"])  # Extract and convert to float
                    # append the score to the list
                    rate_list.append(rate)
                except ValueError as e:
                    logger.warning(f"Skipping invalid row: {row} ({e})")
        
        # Calculate statistics
        stats = {
            "min": min(rate_list),
            "max": max(rate_list),
            "mean": statistics.mean(rate_list),
            "stdev": statistics.stdev(rate_list) if len(rate_list) > 1 else 0,
        }
        return stats
    except Exception as e:
        logger.error(f"Error processing CSV file: {e}")
        return {}

def process_csv_file():
    """Read a CSV file, analyze Ladder score, and save the results."""
    
    # TODO: Replace with path to your CSV data file
    input_file = pathlib.Path(FETCHED_DATA_DIR, "annual_gold_rate.csv")
    
    # TODO: Replace with path to your CSV processed file
    output_file = pathlib.Path(PROCESSED_DIR, "annual_gold_rate_usd_rate.txt")
    
    # TODO: Call your new function to process YOUR CSV file
    # TODO: Create a new local variable to store the result of the function call
    stats = analyze_usd_rate(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:

        # TODO: Update the output to describe your results
        file.write("USD Rate Statistics:\n")
        file.write(f"Minimum: {stats['min']:.2f}\n")
        file.write(f"Maximum: {stats['max']:.2f}\n")
        file.write(f"Mean: {stats['mean']:.2f}\n")
        file.write(f"Standard Deviation: {stats['stdev']:.2f}\n")
    
    # Log the processing of the CSV file
    logger.info(f"Processed CSV file: {input_file}, Statistics saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting CSV processing...")
    process_csv_file()
    logger.info("CSV processing complete.")
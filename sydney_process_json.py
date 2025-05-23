"""
Process a JSON file to count how many years each category is offered as a prize and save the result.

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################


FETCHED_DATA_DIR: str = "sydney_project_data"
PROCESSED_DIR: str = "sydney_project_processed"

#####################################
# Define Functions
#####################################

def count_category_by_year(file_path: pathlib.Path) -> dict:
    """Count the number of years each category was offered as a prize from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:

            # Use the json module load() function 
            # to read data file into a Python dictionary
            category_dictionary = json.load(file)  

            # initialize an empty dictionary to store the counts
            year_counts_dictionary = {}

            # people is a list of dictionaries in the JSON file
            # We can get it using the get() method and pass in the key "prizes"
            prizes_list: list = category_dictionary.get("prizes", [])

            # For each person in the list, get the craft and count them
            for prizes_dictionary in prizes_list:  

                # Get the craft from the person dictionary
                # If the key "craft" is not found, default to "Unknown"
                category = prizes_dictionary.get("category", "Unknown")

                # Update the craft counts dictionary for that craft
                # If the craft is not in the dictionary, initialize it to 0
                # Add 1 to the count for the current craft
                year_counts_dictionary[category] = year_counts_dictionary.get(category, 0) + 1

            # Return the dictionary with counts of astronauts by spacecraft    
            return year_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

def process_json_file():
    """Read a JSON file, count the number of years each category was offered as a prize, and save the result."""


    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "nobel_prize.json")


    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "count_of_times_category_offered_as_prize.txt")
    

    category_counts = count_category_by_year(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write("Number of Years Each Category was Offered:\n")
        for category in category_counts.items():
            file.write(f"{category[0]}: {category[1]}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")
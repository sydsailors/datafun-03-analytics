# datafun-03-analytics

This project will fetch data from the web, process it using appropriate Python collections, and write the processed data to files.

Steps already completed:
1. [Set up the Machine](https://github.com/denisecase/pro-analytics-01/blob/main/01-machine-setup/MACHINE-SETUP.md)
2. [Initialized a new Project](https://github.com/denisecase/pro-analytics-01/blob/main/02-project-initialization/PROJECT-INITIALIZATION.md)

## Before/During Working on the Project
1. Pull the Latest Changes from GitHub 
   
```shell
git pull origin main
```

2. Activate the Project Virtual Environment

```powershell
source .venv/bin/activate
```

3. Install Dependencies As Needed 

```powershell
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt
```

4. Run Script 

```powershell
source .venv/bin/activate
python3 demo-script.py
```

## Add Dependency to requirements.txt
- requests

## Add Files to Retrieve Data from the Web
- yourname_get_csv.py
- yourname_get_excel.py
- yourname_get_json.py
- yourname_get_text.py

## Add Files to Analyze and Process Fetched Data
- yourname_process_csv.py
- yourname_process_excel.py
- yourname_process_json.py
- yourname_process_txt.py

## Description of Files
- [sydney_get_csv.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_get_csv.py) is a CSV file that fetches the CSV file [Annual Gold Rates](https://raw.githubusercontent.com/MainakRepositor/Datasets/refs/heads/master/Gold%20Rates/annual_gold_rate.csv) from the web. 
    - [sydney_process_csv.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_process_csv.py) processes statistics (min, max, mean, standard deviation) from the Annual Gold Rates file in the USD column. 
        - Results: [CSV processed](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_project_processed/annual_gold_rate_usd_rate.txt)
- [sydney_get_excel.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_get_excel.py) is an Excel file that fetches the Excel file [Canada](https://raw.githubusercontent.com/rashida048/Datasets/master/Canada.xlsx) from the web. 
    - [sydney_process_excel.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_process_excel.py) processes the count of occurrences the word "Asia" in a specific column (E) from the Canada file. 
        - Results: [Excel processed](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_project_processed/excel_Canada_Asia_count.txt)
- [sydney_get_json.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_get_json.py) 
    - [sydney_process_json.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_process_json.py)
        - Results: [JSON processed](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_project_processed/json_winners_by_category.txt)
- [sydney_get_text.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_get_text.py) is a text file that fetches the text file [Shakespeare](https://gist.githubusercontent.com/blakesanie/dde3a2b7e698f52f389532b4b52bc254/raw/76fe1b5e9efcf0d2afdfd78b0bfaa737ad0a67d3/shakespeare.txt) from the web. 
    - [sydney_process_text.py](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_process_text.py) processes the count occurrences of the word "thou" from the Shakespeare file. 
        - Results: [Text processed](https://github.com/sydsailors/datafun-03-analytics/blob/main/sydney_project_processed/text_thou_word_count.txt)
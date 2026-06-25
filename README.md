# rbsescrapt
generic form-submission and data-extraction automation example from RBSE website
# Result Portal Automation Example

## Overview

This project demonstrates how to automate form submission, HTML parsing, data extraction, and structured data export using Python.

The script performs the following tasks:

* Submits form data using HTTP POST requests
* Parses HTML responses with BeautifulSoup
* Extracts tabular information from web pages
* Stores records in memory while preventing duplicates
* Exports results to CSV format
* Generates SQL INSERT statements for database import

## Technologies Used

* Python 3.10+
* Requests
* BeautifulSoup4
* Pandas

## Features

### Automated Form Submission

The script sends POST requests to a web form with configurable parameters.

### HTML Parsing

Returned HTML content is parsed using BeautifulSoup to extract structured information.

### Duplicate Prevention

Records are stored in a dictionary keyed by unique identifiers to avoid duplicates.

### CSV Export

Extracted records are saved as a CSV file for analysis or database import.

### SQL Export

The script automatically generates SQL INSERT statements and table creation commands.

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Configure the following variables:

```python
START_ROLL = 1300001
TOTAL_STUDENTS = 5000
YEAR = "2018"
EXAM_TYPE = "SEC_MAIN"
```

Run the script:

```bash
python scraper.py
```

Generated files:

* rbse_results.csv
* insert_students.sql

## Educational Purpose

This project is intended to demonstrate:

* HTTP requests
* Web automation fundamentals
* HTML parsing
* Data cleaning
* CSV generation
* SQL export workflows


## Disclaimer

This project is provided for educational and research purposes only.

The author does not own, operate, endorse, or have any affiliation with any website, service, or data source that may be used with this software.

By using this software, you agree that:

* You are solely responsible for how you use it.
* You will comply with all applicable laws, regulations, website terms of service, and privacy requirements.
* You will obtain any necessary permissions before accessing, collecting, or processing data.
* You will not use this software for unauthorized, unlawful, harmful, or abusive activities.

The author shall not be held liable for any direct, indirect, incidental, consequential, legal, financial, or other damages arising from the use, misuse, or inability to use this software.

Use this software entirely at your own risk.


# Csv Scrape

Instructions: Using python and the requests library, write a scraper that reads a CSV file of addresses, and submits them to this website to check if they are valid or not:
https://tools.usps.com/zip-code-lookup.htm?byaddress
Your output should be the same CSV file as the input, but with an additional column added to it that displays if the address is valid. Please note you can also use other python libraries than the requests library, but your code must use the requests library.

The input data can be downloaded from here:
https://docs.google.com/spreadsheets/d/1H1a9eBamflt3w-4BPEk1kJYc4VgsDBWlDjkS0hV5tAY/edit?usp=sharing



## Requirements

- Python 3.8

## Installation

### Clone Project

```sh
git clone https://github.com/kenyogun/csv-scrape.git
```

### Install Requirements

With a [virtualenv](https://virtualenv.pypa.io/) already set-up, install the requirements with pip:

```sh
pip install -r requirements.txt
```

### Run the application

Start the application by running:

```sh
python run.py
```

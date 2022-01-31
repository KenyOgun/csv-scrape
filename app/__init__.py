"""App module."""

import csv

import requests

PAGE_URL = "https://tools.usps.com/zip-code-lookup.htm?byaddress"
SUBMIT_URL = "https://tools.usps.com/tools/app/ziplookup/zipByAddress"
FILE_NAME = "Python Quiz Input.csv"
HEADERS = {"User-Agent": "custom"}  # use custom user agent to prevent redirect


def get_entries():
    entries = []
    with open(FILE_NAME, mode="r") as fp:
        reader = csv.DictReader(fp)
        entries = list(reader)
    return entries


def check_and_update_entries(entries):
    with requests.Session() as session:
        for entry in entries:
            data_to_submit = {
                "companyName": entry.get("Company"),
                "address1": entry.get("Street"),
                "city": entry.get("City"),
                "state": entry.get("St"),
                "zip": entry.get("ZIPCode"),
            }
            response = session.post(SUBMIT_URL, data=data_to_submit, headers=HEADERS)
            entry["IsValid"] = (
                "FALSE"
                if response.json().get("resultStatus") == "ADDRESS NOT FOUND"
                else "TRUE"
            )
    return entries


def update_csv_with_entries(entries):
    field_names = entries[0].keys()
    with open(FILE_NAME, mode="w", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=field_names)
        writer.writeheader()
        for entry in entries:
            writer.writerow(entry)


def run():
    """Run function."""
    entries = get_entries()

    entries = check_and_update_entries(entries)

    update_csv_with_entries(entries)

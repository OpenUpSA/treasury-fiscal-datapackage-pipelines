# Data Package Pipeline for South African National Budget

This produces a fiscal data package of the South African National Budget directly from the data published on the treasury's website.

This also automatically uploads the fiscal data package to OpenSpending.

## Installation

```
sudo npm install -g os-types
pip install -r requirements.txt
```

## Run

Find the authentication token in the address bar after logging in to OpenSpending

```
GOBBLE_AUTH_TOKEN=... dpp run ./2015-16/estimates-of-national-expenditure-south-africa-2015-16
```

## Provincial

`<province code> - EPRE - <financial year hyphenated> - Final.xlsm` e.g. _"NC - EPRE - 2017-18 - Final.xlsm"_

- Province - code in filename
- Budget year - hyphenated in filename
- List of department names with the sheet label (integers) with its data - sheet "Settings"
- For each department (on their integer-indexed sheet e.g. Education on sheet "1"
  - One-liner description of department C6 which doesn't match what's in the EPRE
  - Table with row for each programme B9 to B28
    - FY-4, FY-3, FY-2 Outcome
    - FY-1 Main Appropriation, Adjusted appropriation, Revised estimate
    - FY
      - Indicative baseline
      - Reprioritised baseline
      - Revised baseline
    - FY+1
      - Indicative baseline
      - Reprioritised baseline
      - Revised baseline
    - FY+2 Indicative baseline
  - Department-level breakdown by economic classification 1, 2, 3
  - For each programme
    - name
    - One-liner description of programme which doesn't match what's in the EPRE
    - Table with row for each sub-programme
      - totals by sub-programme
    - Programme-level breakdon by economic classification 1, 2, 3
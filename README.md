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

### Adding a financial year

We create a file named `fiscal.source-spec.yaml` in a folder tree denoting the financial year and sphere.

To add a new financial year, copy an existing one, updated references to the financial year, and perhaps the source files if their location changed other than the year. Then run `dpp` as shown above.

### Provincial

We scrape the programme-level data from the files with names like `NC - EPRE - 2017-18 - Final.xlsm` from the folders we get from Jonathan. For the above file, the folder would have a name like `2017 MTEF`. The provencance of this data is as follows:

1. The EPRE is the estimates that get tabled. They include actual expenditure from vulindlela and budgeted and forecast expenditure. The budget and forecast come from provincial treasuries (and other provincial departments consolidated), who submit this as spreadsheets according to templates National Treasury give them. This gets transformed into the tables published in the EPRE.
2. The EC - EPRE - 2017-18 - Final.xlsm type-files are the EPRE data, modified to match what was actually passed in the provincial appropriation bills.

#### Generate Provincial Fiscal Data Package

1. Run `python bin/epre.py /path/to/2017 MTEF` if the budget year is 2017.
  - This will generate an `epre-<FY>-<Province Name>.csv` file for each province in the current working directory.
  - How this works is documented further in `epre.py`.
2. Run `dpp` as above using the relevant provincial `fiscal.source-spec.yaml`
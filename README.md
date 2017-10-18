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
GOBBLE_AUTH_TOKEN=... dpp run ./estimates-of-national-expenditure
```
from datapackage_pipelines.wrapper import process
import logging
from pprint import pformat
import re
import requests
import yaml
import os

portal_url = os.environ.get('PORTAL_URL', "https://dynamicbudgetportal.openup.org.za/")


def modify_datapackage(datapackage, parameters, stats):
    logging.info("##### DEADBEEF " + pformat(datapackage))
    # We're not modifying the datapackage but we execute here to execute once
    # before processing rows.
    dataset_name = datapackage['name']
    match = re.match(
        'estimates-of-([a-z]+)-expenditure-south-africa-(\d{4}-\d{2})',
        dataset_name
    )
    sphere = match.group(1)
    year_slug = match.group(2)
    listing_url_path = year_slug + '/departments.yaml'
    listing_url = portal_url + listing_url_path
    r = requests.get(listing_url)
    r.raise_for_status()
    response = yaml.load(r.text)
    departments = response[sphere]
    logging.info("%r", departments)
    return datapackage


def process_row(row, row_index,
                resource_descriptor, resource_index,
                parameters, stats):
    if row['value'] == '':
        row['value'] = '0'
    row['value'] = float(row['value']) * 1000
    return row


process(modify_datapackage=modify_datapackage,
        process_row=process_row)

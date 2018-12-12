from datapackage_pipelines.wrapper import process
import logging
from pprint import pformat
import re
import requests
import yaml
import os
from slugify import slugify

portal_url = os.environ.get('PORTAL_URL', "https://dynamicbudgetportal.openup.org.za/")

department_names = {
    'national': {},
    'provincial': {},
}
warned = {}


def modify_datapackage(datapackage, parameters, stats):
    # We're not modifying the datapackage but we execute here to execute once
    # before processing rows.
    dataset_name = datapackage['name']
    match = re.match(
        'estimates-of-([a-z-]+)(\d{4}-\d{2})',
        dataset_name
    )
    sphere = parameters['sphere']
    year_slug = match.group(2)
    listing_url_path = year_slug + '/departments.yaml'
    listing_url = portal_url + listing_url_path
    r = requests.get(listing_url)
    r.raise_for_status()
    response = yaml.load(r.text)
    for government in response[sphere]:
        department_names[sphere][government['name']] = {}
        for department in government['departments']:
            department_names[sphere][government['name']][department['slug']] \
                = department['name']
        logging.info(department_names)
    return datapackage


def process_row(row, row_index,
                resource_descriptor, resource_index,
                parameters, stats):
    department_slug = slugify(row['department'])
    sphere = parameters['sphere']
    if sphere == 'national':
        government_name = 'South Africa'
    elif sphere == 'provincial':
        government_name = row['government']
    else:
        raise Exception("Unknown sphere: %r" % sphere)
    authoritative_department_name \
        = department_names[sphere][government_name].get(department_slug, None)
    if authoritative_department_name:
        row['department'] = authoritative_department_name
    else:
        warning_key = (government_name, row['department'])
        if warning_key not in warned:
            logging.warn("No authoritative department name found for %s - %s",
                         government_name, row['department'])
            warned[warning_key] = True
    return row


process(modify_datapackage=modify_datapackage,
        process_row=process_row)

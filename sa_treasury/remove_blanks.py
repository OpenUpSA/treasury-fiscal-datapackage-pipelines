"""
Remove rows where the programme or department name is the empty string or 0.

From Jonathan Benjamin:

"The CSV is structure which means there space in each province for 16 departments with 16 programmes (incl. Direct Charges). Each programme has space for 63 lines to accommodate economic classification for each programme. Hence the blanks in some instances."
"""
from datapackage_pipelines.wrapper import process
import logging


def process_row(row, row_index,
                resource_descriptor, resource_index,
                parameters, stats):
    logging.info("%r", row)
    if row['department'] in ('0', '') or row['programme'] in ('0', ''):
        return
    else:
        return row


process(process_row=process_row)

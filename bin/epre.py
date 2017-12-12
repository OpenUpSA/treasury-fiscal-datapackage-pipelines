from openpyxl import load_workbook


wb = load_workbook(filename='../data/provincial/from-jonathan/2015 MTEF/EC - EPRE - 2015-16 - Final.xlsm', read_only=True, data_only=True)
ws = wb['Settings']

department_sheets = []

for row in ws.iter_rows(min_row=13, max_row=13+14):
    print(row[3].value, row[4].value)

from openpyxl import load_workbook


wb = load_workbook(filename='../data/provincial/from-jonathan/2015 MTEF/EC - EPRE - 2015-16 - Final.xlsm', read_only=True, data_only=True)
ws = wb['Settings']

department_sheets = {}

for row in ws.iter_rows(min_row=13, max_row=13+20):
    if row[4].value:
        sheet_name = row[3].value
        department_name = row[4].value
        department_sheets[sheet_name] = department_name
        print(sheet_name, department_name)

for sheet_name, department_name in department_sheets.items():
    ws = wb[str(sheet_name)]

    print("\n", sheet_name, department_name)

    # skip to programmes
    for idx, row in enumerate(ws.iter_rows()):
        if row[1].value == 'PROGRAMME DETAILS':
            programmes_row_idx = idx+1
            break

    for idx, row in enumerate(ws.iter_rows(min_row=programmes_row_idx)):
        if row[1].value and row[1].font and row[1].font.color and row[1].font.color.rgb == 'FF0000FF':
            if row[1].value not in ('Direct Charges'):
                print(row[1].value)

from openpyxl import load_workbook


wb = load_workbook(filename='../data/provincial/from-jonathan/2015 MTEF/NW - EPRE - 2015-16 - Final.xlsm', read_only=True, data_only=True)
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
            programmes_row_idx = idx+2
            break

    economic_classifications = {}
    prev_economic_classification_level = 0
    in_economic_classification = False
    rows = {}
    for idx, row in enumerate(ws.iter_rows(min_row=programmes_row_idx)):
        if row[1].value and row[1].font and row[1].font.color and row[1].font.color.rgb == 'FF0000FF':
            if row[1].value not in ('Direct Charges'):
                programme_name = row[1].value
                print(programme_name)

        if row[1].value == 'Total':
            in_economic_classification = True
            continue
        if row[1].value == 'Total economic classification':
            in_economic_classification = False

        if in_economic_classification:
            economic_classification = row[1].value
            economic_classification_level = int(row[1].alignment.indent)

            if economic_classification_level < prev_economic_classification_level:
                for key, value in list(economic_classifications.items()):
                    if key > economic_classification_level:
                        del economic_classifications[key]

            economic_classifications[economic_classification_level] = economic_classification

            print(economic_classifications)

            rows_key = tuple([department_name, programme_name] + [economic_classifications[k] for k in sorted(economic_classifications)])
            rows[rows_key] = []

            # Drop subtotal that includes this row
            if economic_classification_level > prev_economic_classification_level:
                del rows[prev_rows_key]

            columns = {
                3: 'Outcome',
                4: 'Outcome',
                5: 'Outcome',
                6: 'Main appropriation',
                7: 'Adjusted appropriation',
                8: 'Revised estimate',
                16: 'Budget',
                25: 'MTEF',
                27: 'MTEF',
            }

            for col_idx, phase in columns.items():
                rows[rows_key].append({
                    'phase': phase,
                    'financial_year': ws.cell(row=7, column=col_idx).value,
                    'amount': row[col_idx-1].value,
                })
            print("rows", rows)

            # End
            prev_rows_key = rows_key
            prev_economic_classification_level = economic_classification_level

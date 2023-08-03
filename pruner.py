import os, openpyxl

deletethisrowandbelow = 9

for filename in os.listdir('.'):
    if filename.endswith('.xlsx'):
        wb = openpyxl.load_workbook(filename)
        sheet = wb.active
        sheet.delete_rows(deletethisrowandbelow, sheet.max_row)
        wb.save(filename)
        print('Done with ' + filename)
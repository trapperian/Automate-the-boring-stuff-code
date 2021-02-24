#! python3
# reeadCensusExcel.py - Tabulates population and number of censust tracts for each county.

import openpyxl
import pprint
print('Opening workbooks...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}

print('Reading rows...')
for row in range(2, sheet.max_row + 1):
    #each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

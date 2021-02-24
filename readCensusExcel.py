#! python3
# reeadCensusExcel.py - Tabulates population and number of censust tracts for each county.

import openpyxl
import pprint
print('Opening workbooks...')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
countyData = {}


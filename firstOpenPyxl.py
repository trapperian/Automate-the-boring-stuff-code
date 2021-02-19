import openpyxl

wb = openpyxl.load_workbook("example.xlsx")
print(wb.sheetnames)

sheet = wb["Sheet3"]
type(sheet)

print(sheet.title)

anotherSheet = wb.active
type(anotherSheet)

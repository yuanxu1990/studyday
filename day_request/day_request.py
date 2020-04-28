import requests
import xlrd


url=r"C:\Users\Administrator\Desktop\fund.xls"


workbook=xlrd.open_workbook(url)

print(workbook.sheet_names())

work_sheet=workbook.sheet_by_name('Sheet1')
print(type(work_sheet))
print(work_sheet.nrows)
print(work_sheet.row_values(1))





# Program iterating first column 4 times and timing

import xlrd
import time

print("starting...")

loc = ("top1milURLs.xlsx") 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 

start_time = time.time()
  
for i in range(sheet.nrows):
    if i is None:
        x = (sheet.cell_value(i, 0))

print("--- %s seconds ---" % (time.time() - start_time))

sheet.cell_value(0, 0) 

start_time = time.time()

for i in range(sheet.nrows): 
    x = (sheet.cell_value(i, 0))

print("--- %s seconds ---" % (time.time() - start_time))

sheet.cell_value(0, 0) 

start_time = time.time()

for i in range(sheet.nrows): 
    x = (sheet.cell_value(i, 0))

print("--- %s seconds ---" % (time.time() - start_time))

sheet.cell_value(0, 0) 

start_time = time.time()

for i in range(sheet.nrows): 
    x = (sheet.cell_value(i, 0))

print("--- %s seconds ---" % (time.time() - start_time))
    


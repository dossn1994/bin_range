import csv
import os

try:         
 COL_TO_EXPAND=1
 input_filename = input('Enter the input file name : ')
 output_filename = input('Enter the output file name : ')
 with open(f"{input_filename}", "r") as csvfile:
     csv_reader = csv.reader(csvfile)
     csv_writer = csv.writer(open(f"{output_filename}","w", newline=""))
     head = next(csv_reader)
     csv_writer.writerow(head+["ranged"])
     for row in csv_reader:
         toExpand = row[COL_TO_EXPAND]
         if "(" not in toExpand:
             csv_writer.writerow(row+[toExpand])
         else:    
          fixed = toExpand[:toExpand.index("(")]
          lo, hi = toExpand[len(fixed) + 1 : -1].split("-")
          lower = int(lo)
          upper = int(hi)
          n = len(lo)
          exp = "{0:0"+str(n)+"}"
          for num in range(lower, upper + 1):
           padded_num = exp.format(num)
           modified = row + [fixed.strip() + padded_num]
           csv_writer.writerow(modified)
           
except Exception as e:
 print(e)
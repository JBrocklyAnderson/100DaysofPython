# import libraries
import csv

# initialize the total as a zero-float
total = 0.0

# read in the file
with open("Day54Totals.csv") as file: 
  ## assign contents to variable
  dataTable = csv.DictReader(file) 
  ## apply to every row
  for row in dataTable: 
    ## cumulative addition of the product of each attribute
    total += float(row["Cost"]) * int(row["Quantity"])

print(f"Total: ${round(total,2)}")
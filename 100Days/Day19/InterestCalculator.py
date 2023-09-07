principle = 1000 # total loan amount 
total_amount = principle
total_interest = 0

# anumber of years to repay the loan
for year in range(10):
  interest_for_year = total_amount * 0.05 # 5% APR
  total_amount += interest_for_year
  total_interest += interest_for_year
  print(f"Year {year + 1} is ${round(total_amount, 2)}")
  
print()
print(f"You paid ${round(total_interest, 2)} in interest.")
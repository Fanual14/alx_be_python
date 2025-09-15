monthly_income = float(input ("Enter your monthly income.")) # Input monthly income
monthly_expenses = float(input ("Enter your monthly expenses.")) # Input monthly expenses

monthly_savings = monthly_income - monthly_expenses # Calculate monthly savings
print ("Your monthly savings is:", monthly_savings) 

projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05) # Projected savings after one year with 5% interest

print ("Projected savings after one year, with interest, is:", projected_savings)
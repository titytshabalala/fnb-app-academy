""""
Calculator for drivers to calculate travel costs.
due to petrol prices shifting
"""

# get user travel km

km_travel = float(input("How manay kilometers do you want to drive: "))

# Get current petrol price
petrol_price = float(input("How much is petrol per litre: "))

# Calculate usage
LITERS_NEEDED = km_travel / 10

# Calculate the total cost
total_cost = LITERS_NEEDED * petrol_price

print(f"The total cost is R{round(total_cost,2)}")
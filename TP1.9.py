def electricity_bill(kwh):
    if kwh < 0:
        return None
    
    # Calculate kWh consumed in each progressive tier using min/max logic
    tier1_kwh = min(max(kwh, 0), 50)
    tier2_kwh = min(max(kwh - 50, 0), 150)
    tier3_kwh = max(kwh - 200, 0)
    
    # Compute base consumption cost
    cost = (tier1_kwh * 480) + (tier2_kwh * 610) + (tier3_kwh * 730)
    
    # Add fixed service fee and 10% VAT
    total_riel = (cost + 2000) * 1.10
    
    return round(total_riel)

# Printing the consumption table
test_kwhs = [0, 35, 50, 120, 200, 350]

for kwh in test_kwhs:
    bill_riel = electricity_bill(kwh)
    bill_usd = bill_riel / 4100
    print(f"{kwh:>4} kWh -> {bill_riel:>10,} riel  (≈ {bill_usd:>6.2f} USD)")

# Interactive User Input
user_input = input("Enter your monthly consumption (kWh): ").strip()
try:
    user_kwh = float(user_input)
    bill = electricity_bill(user_kwh)
    if bill is None:
        print("Invalid consumption value.")
    else:
        print(f"Your bill is {bill:,} riel (≈ {bill / 4100:.2f} USD)")
except ValueError:
    print("Please enter a valid numeric value.")
# Get input from the user
waste_per_person = float(input("Waste: "))
holding_capacity = float(input("Cap: "))

# Calculate total waste, land size needed for daily waste, and land size needed for annual waste
population_size = 70000000
total_waste = waste_per_person * population_size

land_for_daily_waste = total_waste / holding_capacity
land_for_annual_waste = land_for_daily_waste * 365

# Convert land size to rai (1 rai = 1600 m^2)
land_for_daily_waste_rai = land_for_daily_waste / 1600
land_for_annual_waste_rai = land_for_annual_waste / 1600

# Display the results
print("Total waste= %.2f" % total_waste)
print("Landfill= %.2f" % land_for_daily_waste_rai)
print("Annual land= %.2f" % land_for_annual_waste_rai)

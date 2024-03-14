def calculate_balance(investment, production, wholesale):
    income = production * 0.001 * wholesale
    balance = income - investment
    return income, balance

investment = float(input("Investment (baht/rai): "))
production = float(input("Rice production (kg/rai): "))
wholesale = float(input("Wholesale price (baht/kwian): "))

income, balance = calculate_balance(investment, production, wholesale)

output_format = "Balance = income ({:,.2f}) - investment ({:,.2f}) = {:,.2f} baht/rai"
print(output_format.format(income, investment, balance))

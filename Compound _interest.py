principal = float(input("Enter principal: "))
rate = float(input("Enter rate: "))
time = int(input("Enter time: "))

amount = principal * (1 + rate / 100) ** time
compound_interest = amount - principal

print("Compound Interest =", compound_interest)
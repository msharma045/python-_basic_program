price = float(input("Enter original price: "))
discount_percentage = float(input("Enter discount percentage: "))

discount = price * discount_percentage / 100
final_price = price - discount

print("Discount =", discount)
print("Final Price =", final_price)
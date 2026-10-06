a = int(input("Enter first subject marks: "))
b = int(input("Enter second subject marks: "))
c = int(input("Enter third subject marks: "))
d = int(input("Enter fourth subject marks: "))
e = int(input("Enter fifth subject marks: "))

total = a + b + c + d + e
average = total / 5
percentage = (total / 500) * 100

print("Total =", total)
print("Average =", average)
print("Percentage =", percentage)
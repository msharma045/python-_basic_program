price = float(input("Enter price: "))
gst_percentage = float(input("Enter GST percentage: "))

gst = price * gst_percentage / 100
final_price = price + gst

print("GST =", gst)
print("Final Price =", final_price)
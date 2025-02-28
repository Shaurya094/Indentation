actual_price = float(input("Enter the actual price of your object: "))
sale_price = float(input("Enter the sale price of your object: "))

if (sale_price > actual_price):
    amount = sale_price - actual_price
    print ("Total profit = {0}".format(amount))
else:
    print ("No profit!")
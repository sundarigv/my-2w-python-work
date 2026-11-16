# Demonstrating user-defined functions - Shopping Bill Calculator

# Input details by user
product = input("Enter product name: ")           # a string value input
price = float(input("Enter product price: £"))    # convert entered value to float using float() predefined method.
quantity = int(input("Enter quantity: "))         # convert entered value to Integer using int() predefined method.

# Userdefined function to calculate total price
def cal_total_price(price, quantity):        # Function with 2 parameters
    total = price * quantity                 # Perform arthematic operation to find total
    return total

# User-defined function to calculate discount
def calculate_discount(total):
    if total >= 100:
        discount = total * 0.10               # based on conditional operator provide 10% disount
    elif total >= 50:
        discount = total * 0.05               # otherwise apply 5% discount
    else:
        discount = 0                          # exit the loop with no discount

    return discount

# Calling user-defined functions
total = cal_total_price(price, quantity)
discount = calculate_discount(total)

final_bill = total - discount

# Display results of total price and applied discount
print("\nProduct:", product)
print("\nTotal Price: £", round(total, 2))       #Used round() function to take decimal precision to 2
print("\nDiscount: £", round(discount, 2))
print("\nFinal Bill: £", round(final_bill, 2))

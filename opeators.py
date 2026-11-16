# Using two or more operators

name = "Roopa"
amount_balance = 25.50
items_In_Cart = 5
is_member = True

# Using List data structure
shopping_list1 = ["Milk", "Bread", "Rice", "Apples", "Sugar"]
shopping_list2 = ["cake", "chocolates", "uiscults"]


# Using Assignment Operator (=) to assign a price value to the list
list_items_price1 = 10.50
list_items_price2 = 2.05

#use + operator to sum oth the list values and assign to a new variable
total_amount= list_items_price1 + list_items_price2

print("Total purchase amount = ", total_amount)

#Using comparision operator and some logical operation
if total_amount > amount_balance :
  print("Insufficient balance")
else:
  amount_balance = amount_balance - total_amount
  print("Remaining available balance is : ",amount_balance)




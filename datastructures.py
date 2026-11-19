#a data structure (e.g. lists, tuples, sets and dictionaries)

name="Roopa"

#Use of List data structure to show items in the cart

shopping_cart=["milk","bread","rice","apples","yogurt","coffee"]      

print("Customer name: ",name)
shopping_cart.sort()             #sorts the list of items in alphaetical order.
print("Items in cart:", shopping_cart)

shopping_cart[2] = "butter"       #update the third item in the List.
print("Items in cart after update : ",shopping_cart)

shopping_cart.append("flour")
print("Items in cart after adding an item : ",shopping_cart)

shopping_cart.remove("rice")
print("Items in cart after removing an item : ",shopping_cart)

shopping_cart[3:4] = ["apples 2", "yougurts 2"] 
print("final list of items in cart after multiple updates : ",shopping_cart)

#Use of Dictonary data structure to store information using key-value pairs

customer_details = {
  "name": "Roopa",
  "amount_balance": 25.50,
  "items_in_cart": 6,
  "is_member" : True
}

print("Customer details using Dictionary data structure", customer_details)         # Print the details of the customer save using Dictionary datastructure
print("Balance amount of customer ",name, "is ", customer_details["amount_balance"])    # Print the individual of the customer from data saved using Dictionary datastructure

#using tuple data structure to store shopping list

list_of_items=("chocolates", "biscults", "cakes")
print("List of items saved using tuples :", list_of_items)

print("First item is : ", list_of_items[0])    #Retieve and print first item from tuple
print("second item is : ", list_of_items[1])    #Retieve and print second item from tuple

# Using Set data structure with duplicate values
shopping_items = {"Milk", "Bread", "Rice", "Milk", "Bread"}

print("Shopping items using set data structure : ",shopping_items)




# Shopping List program to demonstrate the use of while and for loops

shopping_list = []    # Initialise an empty list as a shopping list

# Using a while loop to add multiple products
# Loop continues untill break occurs
while True:
  choice = input("Do you want to add a product? (yes/no): ")    # Choice given to user to add more items by entering 'yes' 
  if choice == "yes":
    item = input("Enter product name : ")   # Used input() method to take product name by user.
    shopping_list.append(item)              # Used a built-in method append() to add items to list.
    
  elif choice == "no":                      # Using condition operator to check if choice entered is 'no'
    break                                   # breaks the loop and exits. 
  else:
    print("Invalid choice, please enter yes/no")
    
# Display total number of products
print("\nTotal products:", len(shopping_list))    #Using Len() predefined method to calculate the numer of items in list.

# Using a for loop to display all products
print("\nYour Shopping List : \n")

for item in shopping_list:             # Iterating through the List item and print each item.
  print(item)

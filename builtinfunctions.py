# student gade calculator demonstrating uil-in fucnctions.

student_name = input("Enter name : ")   # using input() to get the student 
print("Hello, ",student_name)

#using int() function to let user input only numbers.
maths_marks = int(input("Enter Maths marks : "))
english_marks = int(input("Enter english marks : "))
science_marks = int(input("Enter science marks : "))
genKnowlege_marks = int(input("Enter general knowledge marks : "))

marks = [maths_marks, english_marks, science_marks, genKnowlege_marks]  #storing te marks in a list

total_marks = sum(marks)   #using sum function to calculate the total

list_length = len(marks)   #Using len() method to calculate the no of items in list

average = total_marks/list_length   #Using arthematic operation to calculate average

average = round(average, 2)    #Using round() to round the average to 2 decimals

highest_marks = max(marks)   #Using max() method to fetch highest value from the list marks

lowest_marks = min(marks)    #Using max() method to fetch lowest value from the list marks

#decision-making (e.g. if, if-else, if-elf ladder, nested if)
#Program to calculate grades

marks = [75,85,95,35,88,66]       # using list data structure to store marks
result = ""                 # assign an empty value
total_marks = sum(marks)          #using built-in sum() function to calculate the sum of marks
count_marks = len(marks)          #using built-in len() function to calculate the length of list marks

print("Sum is : ",total_marks," and count of the list is : ",count_marks)

average_marks = total_marks/count_marks      # Performing arthematic operation to get average marks value

#Decision-making using if-elif, nested if.

if average_marks>40:                   # using operator graterthan to check the condition and enter the loop 
  if average_marks >=85:               # using operator graterthan equal to check the condition and enter the loop
    result="Grade A"
  elif average_marks < 84 and average_marks >=70: #using comparision operators and also "and" operator to satisfy ot conditions before entering the loop
    result="Grade B"
  elif average_marks < 69 and average_marks >=60:  #using comparision ,  "and" operators
    result="Grade C"
  elif average_marks < 59 and average_marks >=50:  #using comparision ,  "and" operators
    result="Grade D"
  elif average_marks < 49 and average_marks >= 40: #using comparision ,  "and" operators
    result="Grade E"
else:                                       # exit the loop if main condition doesnot satisfy.
  result="Fail"
print("Your percentage of marks is : ",average_marks, " and the obtained result is : ",result)

# Demonstrating the use of time module from Python library
#Calculate the time taken to answer a question in quiz

# Importing time module
import time

print("Welcome to the Python Quiz!")

# Using sleep() from time module to delay the start for 5 seconds
print("Your quiz will start in 5 seconds")
time.sleep(5)

# Record the start time
start_time = time.time()

# Ask the quiz question
answer = input("What is the capital of India? ")

# Record the end time
end_time = time.time()

# Calculate the time taken and round the time to 2 decimal precision using round() defined function
time_taken = round(end_time - start_time, 2)

# Check the answer
if answer.lower() == "delhi":       # Use lower()  function to change all letters of input to lowercase letters
    print("Correct Answer!")
else:
    print("Incorrect Answer!")

# Display the time taken
print("Time taken:", time_taken, "seconds")

# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def checkIfEven(num):
	if num%2 == 0:
		return true
	else:
		return false

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

def printIfEven(num):
	if num%2 == 0:
		print("Even!")
	else:
		print("Odd!")

checkIfEven(num)
printIfEven(num)
# YOUR CODE HERE


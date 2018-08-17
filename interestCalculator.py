# In the first line, we are calling the print() function to display
# an informational message. It is the same as printing like 
# we previously did in the hello world file 
print('Interest Calculator:')

# These next three lines, we're using the following variables to store
# the input provided by the user. The variable 'amount' represents
# the principal amount borrowed.
amount = float(input('Principal amount ?'))

# 'roi' represents the rate of interest levied on the principal amount.
# float(value) -> It converts a value to a float type number.
roi = float(input('Rate of Interest ?'))

# 'years' represents the number of years of the borrowing period
# int(value) -> It converts any value to a plain integer.
years = int(input('Duration (no. of years) ?'))

# Using the variable 'total', we can store the result of the complex assignment
# The total -> It represents the total amount to be paid after the borrowing period.
total = (amount * pow(1 + (roi/100), years))

# Further to add, this assignment involves the use of the following Python’s arithmetic operators and functions.
# + Addition -> It adds numbers on either side of the operator.
# * Multiplication -> It multiplies numbers on either side of the operator.
# / Division -> It divides left-hand operand by right-hand operand.
# pow(X, Y, Z) -> It determines [X to the power Y]. If Z is available, then it’ll return X to the power Y, modulo Z.

# Use Python's subtraction operator to calculate the interest amount
interest = total - amount

# Finally, there is a print statement displaying the interest amount. Since it is a 
# float value, so the print() function will show the full number by default. 
# Hence, we are using the floating point format specifier “%0.2f” in print() function 
# so that we can limit the printing up to two decimal points.
print('\nInterest = %0.2f' %interest)

# To see the output in Terminal, right click the file and select 'Run Python File in Terminal'
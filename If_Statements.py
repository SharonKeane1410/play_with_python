number = 5
if number == 5 :
    print("Number is 5")
else:
    print("Number is not 5")

#Truthy and Falsy values:
if number: # just checks that the variable is defined: which it is so it is truthy
    print("Number is defined and 'Truthy'")

text = "Python"
if text: # just checks that the variable is defined: which it is so it is truthy
    print("Text is defined and 'Truthy'")

python_file = True
if python_file: # just checks that the variable is defined: which it is so it is truthy
    print("This will execute")

aliens_found = None
if aliens_found:# just checks that the variable is defined: which it is NOT so it is falsy and the statement will not execute
    print("This will not execute as 'None' is 'falsy'")

#check if condition is false avoids having to create a true statment and putting logic in the else section
if number != 5:
    print ("This will not execute")

if not python_file:
    print("This will not execute")

# linking multiple if conditions
if number == 5 and python_file:
    print("This will execute as both conditions are true")

if number == 17 or python_file:
    print("This will execute as only one condition needs to be true")

#ternary if statements
a = 1
b = 2

"bigger" if a > b else "smaller"

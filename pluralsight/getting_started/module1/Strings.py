#py 2 unicode
# py3 ASSCI

#defining strings
# single, double or triple quotes
'Hello World' == "Hello World" == """Hello World"""

#string methods
"hello".capitalize() == "Hello"
"hello".replace("e", "a") == "hallo"
"hello".isalpha() == True
"123".isdigit() == True #can be used to covert to int

"some,random,values".split(",") == ["some", "random", "values"]

#String Formatiing
name = "Sharon"
machine = "Lenovo"

#string format passing variables as args to the format fuction and referencing the position
"Nice to meet you {0}. I am {1}".format(name, machine)
#string interpolation - prefix the string with f char outside of the string and use the variables by name
f"Nice to meet you {name}. I am {machine}"


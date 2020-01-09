#create prepopulated list and print each element
student_name = ["Mark", "Kate", "Jessica"]
print(student_name[0])
print(student_name[1])
print(student_name[2])
#For Loops
for name in student_name:
    print("Student name is {0}".format(name))

x = 0
for index in range(10):
    x += 10
    print("The value of X os {0}".format(x))

#range supports a starting point, end point and increment value
range (5, 10, 2 ) == [5, 7, 9]

#While Loops
x = 0
while x < 10:
    print("Count is {0}".format(x))
    x += 1
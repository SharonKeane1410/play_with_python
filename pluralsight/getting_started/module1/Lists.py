#create empty list
student_name = []
#create prepopulated list
student_name = ["Mark", "Kate", "Jessica"]
#Use position to reference list element
student_name[0] == "Mark"
student_name[-1] == "Jessica" # first element from right aka last element
#replacing or overwrite element in the list
student_name[0] == "James"
#add to a list, adds to the end of exsisting list
student_name.append("Homer")
#check is an element exsists already
"Mark" in student_name == True
#count elements in list
len(student_name) == 4
#delete an element, remove Jessica and move element to the right back one space
del student_name[2]
#list slicing > does not alter the origional list
student_name[1:] = ["Kate", "Homer"] # gives all elements from position 1 onwards
student_name[1:-1] = ["Kate"] # removes first and last


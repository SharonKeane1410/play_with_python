student = {
    "name": "Mark",
    "Student_id" : 15163,
    "feedback": None
}
# produces a KeyError
#last_name = student["last_name"]
try:
    last_name = student["last_name"]
except KeyError:
    print("Error Finding last_name.")

student["last_name"] = "Keane"
try:
    last_name = student["last_name"]
    add_int_to_last_name = 3 + last_name
except KeyError:
    print("Error Finding last_name.")
except TypeError as error:
    print("I cannot add these two together")
    print(error)
#except Exception: # catch all exception handling
#    print("Unknown error :(")

print("The 'try block' threw a TypeError Exception so the 'except block' caught it and handled it")

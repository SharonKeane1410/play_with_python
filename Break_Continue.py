student_name = ["James", "Katarina", "Jessica", "Mark", "Bort", "Frank Grimes", "Max Power"]
print("Checks ALL Elements in the List for 'Mark' even after finding it will stay looking")
for name in student_name:
    if name == "Mark":
        print("Found him! " + name)
    print("Currently testing " + name)

print("Checks Elements in the List for 'Mark' until found")
for name in student_name:
    if name == "Mark":
        print("Found him! " + name)
        break
    print("Currently testing " + name)

print("Checks for ALL Elements in the List except 'Bort'")
for name in student_name:
    if name == "Bort":
        continue
        print("Found him! " + name)
    print("Currently testing " + name)

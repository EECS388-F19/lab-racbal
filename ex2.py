
students = ["Kelsey", "Yeon", "Alex"]

students.sort()

for el in students:
    print(el)

# OR:
print(students)

first_name = students[0]

first_name = first_name[:-1]

print(first_name)

longname = ""
for el in students:
    if len(el) > len(longname):
        longname = el
print(longname)

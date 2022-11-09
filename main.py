# Two ways of zip to get a list:
# First way :
students_id = (1,2,3,50,20,10,25)
students_name = {"Humayun", "Monir", "Bishal", "Kabir", "Aminur","Azay", "Avinash"}
students_grade = (3.50,3.90,3.74,3.75,3.00,2.92,3.88)
students_result = zip(students_id,students_name,students_grade)
print(list(students_result))

# Second Way:
students_id= (1,2,3,50,20,10,25)
students_name={"Humayun", "Monir", "Bishal", "Kabir", "Aminur","Azay", "Avinash"}
students_grade=(3.50,3.90,3.74,3.75,3.00,2.92,3.88)
for i1, i2,i3 in zip(students_id,students_name,students_grade):
    print(i1, i2,i3)

# Enumerate exercise:
names = ["Rachael Green", "Goodfellow Ian", "Tedd Crock", "Mina Joseph"]
salaries = [10260, 41571, 71211, 52141, 35781]
people_salaries = []

# ***** Here  j in enumerate(names) implies the j variable is related to names.****

for i, j in enumerate(names):
    x = j + " $" + str(salaries[i])
    people_salaries.append(x)
print(people_salaries)

# upgration of last one:
names = ["Rachael Green", "Goodfellow Ian", "Tedd Crock", "Mina Joseph"]
salaries = [10260, 41571, 71211, 52141, 35781]
people_salaries = []
for i, j in enumerate(names):
    x=j+ " § " + str(salaries[i])
    people_salaries.append(x)
print(people_salaries)
# List comprehension :
my_list_normal= []
for current_element in range(10):
    my_list_normal.append(current_element)
print(my_list_normal)
# Comprehensive list  in one line:
my_list_comp=[current_element for current_element in range(10)]
print(my_list_comp)
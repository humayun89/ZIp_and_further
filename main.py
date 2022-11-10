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
# Same as the letter one:
expenses=[]
for i in range(1550,2000,200):
    expenses.append(i)
print(expenses)
# now:
expenses=[i for i in range(1550,2000,200)]
print(expenses)

# Again:
list_comp =  [ (index , value ) for index ,value in enumerate( range( 5, 10 ) ) ]
print(list_comp)
# My practise:
Students_cgpa=(3.50,3.70,3.94,3.77)
cgpa=[(student_rank, result) for student_rank, result in enumerate(Students_cgpa,1)]
print(cgpa)
# more
Dictionary1 = { 'A': 'Geeks', 'B': 4, 'C': 'Geeks' }
items= Dictionary1.items()
del[Dictionary1['C']]
print(items)
# quiz from Udemy:
students_dict = {
                    "Joel Corry" : 70,
                    "James Bond" : 90,
                    "Fatma Ahmed": 20,
                    "Lily Saqr"  : 94,
                    "Ahmed Yan"  : 40,
                }
passed_students_names = [name.split()[0] for name, x in students_dict.items() if x > 50]
print(students_dict)
# Own made problem using split() : find those expenses less than 200.
monthly_expenses = {
                    "house_rent" : 5000,
                    "electricity" : 200,
                    "fuel_costs" : 650,
                    "meal_expenses" : 300,
                    "cigarette" : 100,
                    "coffee" : 50,
                   }
except_smaller_expenses = [expenses.split()[0] for expenses, i in monthly_expenses.items() if i > 200]
print(except_smaller_expenses)

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
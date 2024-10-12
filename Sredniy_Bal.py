grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
#print(type(grades))
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
#(type(students ))
sredniy_bal = {'test' : 1}
#print(sredniy_bal)
#print(sorted(students))
#sr_grades = [1, 1,]
sr_grades = [[sum(grades[0])/len(grades[0])], [sum(grades[1])/len(grades[1])], [sum(grades[2])/len(grades[2])], [sum(grades[3])/len(grades[3])], [sum(grades[4])/len(grades[4])]]
#print(type(sr_grades))
sredniy_bal = dict(zip(sorted(students), sr_grades))
print(sredniy_bal)









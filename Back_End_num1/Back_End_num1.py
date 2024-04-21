#def num1():
your_text=input("ВВедите строку :\n")
print(your_text[::-1])

#2
your_text=input("ВВедите строку с h :\n")
print(your_text[0]+ your_text[1:-1].replace('h','H')+ your_text[-1])

#3
your_text=input("ВВедите строку  :\n")
words=your_text.split()
num_words=len(words)
print(num_words)

#4
your_text=input("ВВедите строку  :\n")
import re
import string
res=re.findall(r"\w+",your_text)
pip=len(res)
print(pip)

#5
your_text=input("ВВедите строку  :\n")
arr=your_text.split(' ')
res= arr[1] + " " + arr[0]
print(res)
 
#6
your_text=input("ВВедите строку  :\n")
arr=your_text.split(' ')
res=arr[0]+ ' ' +arr[1][0] + '.' +arr[2][0] + '.'
print(res)

#7
l = [5,[5.5,[5j,[[],5,"Иголка"]]]]
print(l[1][1][1][2])

#8
l1=[1,1,1]
l2=[4,4,4]
l1.extend(l2)
print(l1)
print(l1+l2)

#9
l1=[4,5,6]
l2[1,2,3,7,8]
l3=l1+l2
l3.sort()
l3=list(set(l3))
print(l3)

#10
l1 = [1,2,3,4,5]
l2 = [2,2,4,5,5]
l3 = list(set(l1))
l4 = list(set(l2))
print(len(l1) == len(l3))
print(len(l2)==len(l4))

#11
date_dict = {'year': 2024, 'month': 4, 'day': 14}
print(str(date_dict['year']) + '-' + str(date_dict['month']) +'-'+ str(date_dict['day']))

#12
string=str(input())
arr = string.split(',')
kort  = tuple(arr)
print(arr)
print(kort)

#13
students = {'Schultz', 'Django', 'Brunhilde', 'Fritz'}
employees = {'Schultz', 'Django', 'Calvin', 'Butch', 'Fritz'}
print(students | employees)
print(students.union(employees))
print(students & employees)
print(students.intersection(employees))
print(employees - students)
print(employees.difference(students))
print(students ^ employees)
print(students.symmetric_difference(employees))

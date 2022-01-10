#first question to find average
print('Question 1')

num1=float(input('Enter first number.'))
num2=float(input('Enter second number.'))
num3=float(input('Enter third number.'))

#using simple mean formula
avg=(num1+num2+num3)/3

print('Average of the three numbers is', avg)

#second question to find income tax
print('Question 2')

g_income=float(input('Enter your gross income.'))
dep=int(input('Enter the number of dependents you have.'))

#using fomula of income tax given in question
tax=(g_income-10000-3000*dep)/5

print('The income tax you have to pay is $',tax , sep="")
    
#third question to store different data types
print('Question 3')

sid=int(input('Enter student ID.'))
s_name=str(input('Enter student name.'))
gender=str(input('Enter gender:M,F or U(Unknown).'))
course=str(input('Enter course name.'))
cgpa=float(input('Enter CGPA'))

#creating a list to store the different data types
student=[sid,s_name,gender,course,cgpa]
print(student)

#fourth question to create and sort list
print('Question 4')

mlist=[]
#creating an empty list to add values in

for k in range(1,6):
    #for loop to take 5 inputs from the user to append in the list
    marks=float(input('Enter marks of student no.'+ str(k)+':'))
    mlist.append(marks)

mlist.sort(reverse=True)
#to sort the list in ascending order
print(mlist)

#fifth question to add or delete elements from a list
print('Question 5a')
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#deleting 4th element, i.e. black 
del(color[3])
print(color)

print('Question 5b')
color=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#replacing 4th and 5th elements with a single element
color[3]='Purple'; del(color[4])
print(color)
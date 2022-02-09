#ITC assignment 3
#Yuvraj Singh Birdi
#CSE
#21103049

#Question 1
print('Question 1.')
string1=str(input('Enter the string to calculate the occurrence of characters/words:')) #input string
if ' ' not in string1: #single word, finding occurrence of characters
    count1={} #dictionary to store occurence of each character
    for char in string1:
        if char in count1:
            count1[char]+=1 #if character already in dictionary, increase count
        else:
            count1[char]=1 #otherwise, add character as key and put 1 as the value
    print(count1)
elif ' ' in string1: #multiple words, finding occurrence of words
    count2={} #dictionary to store occurrence of each word
    words=string1.split() #list containing each word from input string
    for word in words:
        if word in count2:
            count2[word]+=1 #if word already in dictionary, increase count
        else:
            count2[word]=1 #otherwise, add word as key and put 1 as the value
    print(count2)

#Question 2
print('Question 2.')
while True:
    year=int(input('Enter a year:')) #input year
    if 1800<=year<=2025: #given condition for year
        break
    else:
        print('Enter year from 1800-2025!')
#to check whether leap year
if year%400==0: 
    leap=True
elif year%100==0: #for years divisible by 100, they need to be divisible by 400 to be leap
    leap=False
elif year%4==0: 
    leap=True
else:
    leap=False
while True:
    month=int(input('Enter a month:')) #input month
    if 1<=month<=12: #given condition for month
        break
    else:
        print('Enter month from 1-12!')
if month in (1,3,5,7,8,10,12): #these months have 31 days
    month_length=31
elif month==2: #for february
    if leap==True:
        month_length=29 #february days in leap year
    else:
        month_length=28 #february days in non-leap year
else:
    month_length=30 #days in other months are 30

while True:
    day=int(input('Enter a day:')) #input day
    if day>month_length: 
        print('Enter a day according to the month entered!')
    if 1<=day<=month_length: #day needs to be less than equal to length of entered month
        break
if day<month_length:
    day+=1 #it is not last day of month, just add one
else:
    day=1 #it is last day of month, next day will be 1st
    if month==12:
        month=1 
        year+=1 #it is last month of year also, next month is Jan and add one in year
    else:
        month+=1 #it is not last month of year, just add one to it
print('Next date from entered date is %d/%d/%d.' %(day,month,year))

#Question 3
print('Question 3.')
list1=[] #empty list for including input values
while True:
    num=input('Enter number to find square(enter nothing to print output):') #input number
    if num=='':
        break
    list1.append(int(num)) #adding input number to the list
print('Entered values are ',end='')
print(list1) #displaying list of entered values
print('The list of tuples is:',end='')
print([(i,i**2) for i in list1]) #squaring each value of list and displaying a list of tuples of (input number,it's square)

#Question 4
print('Question 4.')
letter_grade={10:'A+',9:'A',8:'B+',7:'B',6:'C+',5:'C',4:'D'} #dictionary containing letter corresponding to grade
performance={10:'outstanding',9:'excellent',8:'very good',7:'good',6:'average',5:'below average',4:'poor'} #dictionary containing remarks corresponding to grade
while True:
    grade=int(input('Enter your grade point(between 4 and 10):')) #input grade
    if 4<=grade<=10: #given condition
        break
    else:
        print('Error: Enter a grade point between 4 and 10!') #error message
print('For your grade point %d:' %grade) 
print('Your grade is %s and your performance is %s.' %(letter_grade[grade],performance[grade])) #printing letter and remark corresponding to input grade from the dictionary

#Question 5
print('Question 5.')
letters=['A','B','C','D','E','F','G','H','I','J','K'] #defined list of alphabets
for i in range(6): #as six lines of output required
    print(' '*i, end='') #for altering spaces at front corresponding to i
    for j in range(len(letters)-2*i): #2 letters are being taken out in each line
        print(letters[j],end='') #printing the required letters from list 
    print(' '*i) #for altering spaces at end corresponding to i

#Question 6
print('Question 6.')
sno=1 #serial number of value
dict1={} #dictionary to store values
while True:
    student_name=input("Enter student %d's name:" %sno)
    sid=int(input("Enter student %d's SID:" %sno))
    dict1[sid]=student_name #storing name as value and SID as key
    option=str(input('Would you like to enter more data?(y/n)'))
    if option in ['Y','y']:
        sno+=1
        continue
    if option in ['N','n']:
        break
print('<A> Student details in dictionary:\n', dict1) #in order of entering 
print('<B> Sorted according to names:\n', dict(sorted(dict1.items(), key=lambda item: item[1]))) #dict1 sorted alphabetically according to value,i.e. names
print('<C> Sorted according to SID:\n', dict(sorted(dict1.items()))) #dict1 sorted in ascending order according to key, i.e. SID
search_sid=int(input('<D> Enter SID for student name:')) 
print(dict1[search_sid]) #student name corresponding to the SID entered by the user

#Question 7
print('Question 7.')
nterms=int(input('Upto how many terms to print Fibonacci sequence:'))
n1,n2=0,1 #first two terms
count=0 
sum_nums=0 
while count<nterms: #generate fibonacci sequence upto nterms
    print(n1)
    sum_nums+=n1
    nth=n1+n2
    n1=n2 #update values
    n2=nth
    count+=1
avg=sum_nums/nterms #to find average of numbers upto nterms
print('Average of resultant Fibonacci series is ',avg)

#Question 8
print('Question 8.')
set1={1,2,3,4,5} #given sets
set2={2,4,6,8}
set3={1,5,9,13,17}
#using set theory
print('<A> ', (set1|set2)-(set1&set2)) #elements in set1 and set2 but not both
print('<B> ', (set1|set2|set3)-((set1&set2)|(set2&set3)|(set3&set1))) #elements only in one of the three given sets
print('<C> ', ((set1&set2)|(set2&set3)|(set3&set1))-(set1&set2&set3)) #elements exactly in two of the given three sets
set4={1} #defining new set
for i in range(2,11):
    set4.add(i) #containing elements from 1 to 10
print('<D> ', set4-set1)  #elements in 1 to 10 but not in set1
print('<E> ', set4-(set1|set2|set3)) #elements in 1 to 10 but not in set1,set2 and set3


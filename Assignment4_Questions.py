#ITC Assignment 4
#Yuvraj Singh Birdi
#CSE
#21103049

#Question 1
print('Question 1')
#Recursive python function to solve the Tower Of Hanoi problem

def TowerOfHanoi(n , source, destination, auxiliary): 
#n is the number of disks, source is the rod on which all disks are initially, destination is the rod that all disks need to be on finally and auxilliary is the remaining rod  
	if n==1:
		print ("Move disk 1 from rod",source,"to rod",destination) #moving last disk to C
		return
	TowerOfHanoi(n-1, source, auxiliary, destination) #moving n-1 disks from A to B
	print ("Move disk",n,"from rod",source,"to rod",destination) #moving nth disk from A to C
	TowerOfHanoi(n-1, auxiliary, destination, source) #moving n-1 disks from B to C
		
TowerOfHanoi(3,'A','C','B')
#3 disks, initial rod=A, final rod=C, middle/auxilliary rod=B

#Question 2
print('Question 2')
n=int(input("Enter number upto which you want to print Pascal's Triangle:"))

#using recursion:
def pascal_triangle(n):
    if n == 0:
        return []
    elif n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n-1) #recursive statement
        last_row = result[-1]
        for i in range(len(last_row)-1):
            new_row.append(last_row[i] + last_row[i+1])
        new_row += [1]
        result.append(new_row)
    return result

print('Using recursion:')
for i in pascal_triangle(n): #pascal_triangle returns a list of lists of each row of pascal's triangle
    for j in i:
        print(j,end=' ') #printing in required format
    print('')

#Using iteration
def factorial(n):  #defining factorial of a number
    if n == 0:
        return 1
    else:
        fact=1
        for i in range(1,n + 1):
           fact=fact*i
        return fact

def C(n,r): #defining combination of nCr 
    return int(factorial(n)/((factorial(n-r))*(factorial(r))))

print('Using Iteration:')
i=0
while i<n:
    for j in range(0,i+1):
        print(C(i,j),end=' ') #printing in required format
    print('')
    i+=1

#Question 3
print('Question 3')
while True:
    a,b=map(int,input('Enter two values a and b separated by single space:').split())
    if b==0:
        print('Division by zero is not defined!')
    else:
        break

print('Quotient and remainder for entered value is:', divmod(a,b)) #built-in divmod function returns a tuple (a//b,a%b), i.e. quotient and remainder
print('<A> Is function callable:',callable(divmod(a,b))) #using built-in callable function 
print('<B> Are entered values nonzero:', end=' ')
if max(divmod(a,b))==0: #manipulating built-in max function for tuple to find whether non-zero value is entered(both Q and R are 0 when 0 is divided)
    print('No')
else:
    print('Yes')
print('<C> Adding (4,5,6) to it:',end=' ')
l=list(divmod(a,b)) #using built-in list function for converting to list and manipulating it
l+=[4,5,6]
t=tuple(l) #using built-in tuple function to convert back to tuple
print(t, end=' ')
print('and after filtering values > 4:',end=' ')
l_=[]
for i in l:
    if i<=4:
        l_+=[i] 
t_=tuple(l_) #new tuple from list with values <=4 using built-in tuple function
print(t_)

print('<D> Converting to set datatype:',set(t_))
print('<E> Making the set immutable:',frozenset(set(t_)))
print('<F> Maximum value from set is:',max(frozenset(set(t_))), 'and its hash value is:',hash(max(frozenset(set(t_)))))

#Question 4
print('Question 4')

class student:
    def __init__(self,name,sid):
        self.name=name
        self.sid=sid
    def display(self):
        print('Name is '+self.name+' and SID is '+str(self.sid))
    def __del__(self):
        print('Destroyed created object')

name1=str(input('Enter your name:'))
sid1=int(input('Enter your SID:'))

s1=student(name1,sid1)
s1.display()

del s1

#Question 5
print('Question 5')

class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print('Name is '+self.name+' and salary is '+str(self.salary))

employee1=employee('Mehak',40000)
employee1.display()

employee2=employee('Ashok',50000)
employee2.display()

employee3=employee('Viren',60000)
employee3.display()

print('<A> Updated:',end='')
employee1.salary=70000
employee1.display()

print('<B>',end=' ')
del employee3
print('Record of Viren deleted.')

#Question 6
print('Question 6')

def anagram(word):
    if len(word)==1:
        return [word]
    partial_words=anagram(word[1:])
    char=word[0]
    result=[]
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result        


George_word=input("Word uttered by George:")
Possible_words=anagram(George_word)
Barbie_word=input("Word spoken by Barbie:")
print("Possible Words:",Possible_words)
print("If Barbie's word lies in the list,then their friendship is real.")

if Barbie_word in Possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")




    












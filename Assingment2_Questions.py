
print('Answer 1')
s_input="Python is a case sensitive language"

print('a.', end=' ')
#ques1(a) part to find length of string
l=len(s_input)
print(l)

print('b.', end=' ')
#ques 1(b) to reverse the order in one line code
s_input_reverse=s_input[::-1]
#arranging the string starting from the back using slice function
print(s_input_reverse)

print('c.', end=' ')
#ques 1(c) to form new string using slice function
s_input_new=s_input[10:26]
print(s_input_new)

print('d.', end=' ')
#ques 1(d) to replace part of s_input using slice function
#note: strings are immutable so we form a new string 
s_input_replaced=s_input[0:10]+'object oriented'+s_input[26:35]
print(s_input_replaced)

print('e.', end=' ')
#ques 1(e) to find index of "a" in s_input
a_index=s_input.index('a')
print(a_index)

print('f.', end=' ')
#ques 1(f) to remove white spaces from s_input
s_input_removed=s_input[0:6]+s_input[7:9]+s_input[10:11]+s_input[12:16]+s_input[17:26]+s_input[27:35]
print(s_input_removed)

print('Answer 2')
#Use of string formatting to print given output
name='Yuvraj Singh Birdi'
sid=21103049
dep_name='CSE'
cgpa=9.90
print('Hey, %s here!' %name)
print('My SID is %d' %sid)
print('I am from %s department and my CGPA is %.2f' %(dep_name , cgpa))

print('Answer 3')
#Use of bitwise operators
a=56
b=10

print('a.', end=" ")
#Using 'and' operator between a and b
ans_a=a&b 
print(ans_a)

print('b.', end=" ")
#Using 'or' operator between a and b
ans_b=a|b
print(ans_b)

print('c.', end=" ")
#Using 'xor' operator between a and b
ans_c=a^b
print(ans_c)

print('d.', end=" ")
#Using '<<' left shift operator
ans_d_1=a<<2
ans_d_2=b<<2
print('a would become %d and b would become %d' %(ans_d_1,ans_d_2))

print('e.', end=" ")
#Using '<<' left shift operator
ans_e_1=a>>2
ans_e_2=b>>4
print('a would become %d and b would become %d' %(ans_e_1,ans_e_2))

print('Answer 4')
#To find the largest of three numbers using list sorting
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
c=int(input('Enter third number: '))
numbers=[a,b,c]
numbers.sort(reverse=True)
ans_4=numbers[0]
print(ans_4, ' is the largest number.')

print('Answer 5')
#To check whether 'name' is present in the entered string
word=str(input('Enter a word to check: '))
if 'name' in word:
    print('Yes')
else:
    print('No')

print('Answer 6')
#To check whether entered lengths can be used to form a triangle 
l_1=int(input('Enter length of first side: '))
l_2=int(input('Enter length of second side: '))
l_3=int(input('Enter length of third side: '))
if l_1>=l_2+l_3 or l_2>=l_1+l_3 or l_3>=l_1+l_2:
    print('No')
else:
    print('Yes')

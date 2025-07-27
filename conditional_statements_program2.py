#1.Check whether a number is positive, negative, or zero and even/odd.
"""
n=int(input())
if (n>0) and (n%2==0):
    print(f'{n} is positive even number')
elif (n<0) and (n%2==0):
    print(f'{n} is negative even number')
elif (n>0) and (n%2!=0):
    print(f'{n} is positive odd number')
elif (n<0) and (n%2!=0):
    print(f'{n} is negative odd number')
else:
    print(f'{n} is either even or odd')
"""
#2.Assign grades based on marks (90+: A+, 80-89: A, etc.).
"""
marks=int(input())
if ((marks>=90) and (marks<=100)):
    print('A+ grade')
elif ((marks>=80) and (marks<=89)):
    print('A grade')
elif ((marks>=70) and (marks<=79)):
    print('B+ grade')
elif ((marks>=60) and (marks<=69)):
    print('B grade')
elif ((marks>=50) and (marks<=59)):
    print('C grade')
elif ((marks>=40) and (marks<=49)):
    print('D grade')
elif (marks>=101):
    print("enter values upto range 100")
else:
    print("below average")
"""
#3.Create a simple calculator using +, -, *, / operators.
"""
a,b=map(int,input().split())
operator=input()
if operator=="+":
    print(a+b)
elif operator=="-":
    print(a-b)
elif operator=="*":
    print(a*b)
elif operator=="/":
    print(a/b)
else:
    print("invalid operator")
"""
#4.Check whether a triangle is valid based on the sum of its angles
"""
a,b,c=map(int,input().split())
if (a+b+c==180):
    print("a,b,c can form triangle")
else:
    print("not possible to form triangle")
"""
#5.Check if a number is divisible by 3 and 5.
"""
n=int(input())
if (n%3==0 and n%5==0):
    print(f'{n} is divisible by both 3 and 5')
elif (n%3==0):
    print(f'{n} is divisible by 3')
elif (n%5==0):
    print(f'{n} is divisible by 5')
else:
    print(f'{n} is not divisible by both 3 and 5')
"""

#6.Determine if a number is a three-digit number.
"""
n=int(input())
if (n>=100 and n<1000):
    print(f'{n} is a three digit number')
else:
    print(f'{n} is not a three digit number')
"""

#7.Check if a number is even and multiple of 7.
"""
n=int(input())
if (n%2==0 and n%7==0):
    print(f'{n} is even and multiple of 7')
elif (n%2==0):
    print(f'{n} is even but not multiple of 7')
elif (n%7==0):
    print(f'{n} is multiple of 7 but not even')
else:
    print(f'{n} is not even and not multiple of 7')
"""
#8.Determine the type of triangle (Equilateral, Isosceles, Scalene) using sides.
"""
s1,s2,s3=map(int,input().split())
if (s1==s2==s3):
    print("it is equilateral triangle")
elif (s1 == s2 or s2 == s3 or s3 == s1):
    print("it is isosceles triangle")
else:
    print("it is scalene triangle")
"""
#9.Check if a number is within a range (50-100)
"""
n=int(input())
if (n>=50 and n<=100):
    print(f'{n} is in range betweeen 50 and 100')
else:
    print(f'{n} not in range of 50 and 100')

"""

#10.Check whether a given year is a century year
"""
n=int(input())
if (n%100==0):
    print(f'{n} is a century year')
else:
    print(f'{n} is not a century year')
"""
#11.Compare two numbers and display the greater and the difference
"""
a,b=map(int,input().split())
if (a>b):
    print(f'{a} is greater')
else:
    print(f'{b} is greater')
print("the difference is:", a-b)
"""

#12.Check if a day number (1–7) corresponds to weekday or weekend.
"""
string=str(input())
s=int(string)
if (s==1):
    print(f'{s} is sunday and it is weekend')
elif (s==2):
    print(f'{s} is monday and it is weekday')
elif (s==3):
    print(f'{s} is tuesday and it is weekday')
elif (s==4):
    print(f'{s} is wednesday and it is weekday')
elif (s==5):
    print(f'{s} is thursday and it is weekday')
elif (s==6): 
    print(f'{s} is friday and it is weekday')
elif (s==7):
    print(f'{s} is saturday and it is weekend')
else:
    print("not valid number")
"""
#13.Check if three sides can form a right-angled triangle.
"""
a,b,c=map(int,input().split())
if (c==(a**2+b**2)**0.5):
    print("it is right angle triangle")
else:
    print("not possible")
"""
#14.Find the roots of a quadratic equation and display their nature.
"""
a,b,c=map(int,input().split())
n=(b**2-4*a*c)**0.5
D=(b**2-4*a*c)
d=2*a
r1=(-b+n)/d
r2=(-b-n)/d
if (D>0):
    print("the 2 roots are real and distinct roots")
elif (D==0):
    print("the 2 roots are real and equal roots")
else:
    print("no real roots")
"""
















































































    


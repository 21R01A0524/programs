#convert km into miles
km=float(input())
miles=km/1.609
print(miles)

#miles to km
miles=float(input())
km=1.609*miles
print(km)

#convert celsius into fahrenheit
c=float(input())
f=c*9/5+32
print(str(f)+" F")#36->96.8 F


#convert fahrenheit into celsius
f=float(input())
c=(f-32)*5/9
print(str(c) + " C")#96.8->36.0 C
"""
"""
# to get output in integer form
f=float(input())
c=(f-32)*5/9
ce=int(c)
print(str(ce) + " C")#96.6->36


#calendar
import calendar
year=int(input())
month=int(input())
print(calendar.month(year,month))#for single month


import calendar
year=int(input())
print(calendar.calendar(year))#for all months

#quadratic equation
a=int(input())
b=int(input())
c=int(input())
#a,b,c=map(int,input().split())
n=(b**2-4*a*c)**0.5
d=2*a
r1=(-b+n)/d
r2=(-b-n)/d
print(r1,r2)
#print(r2)
"""





























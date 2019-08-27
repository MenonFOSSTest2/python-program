name=input("enter your name")
roll_no=input("enter your rollno")
address=input("enter your address")
a=int(input("Enter the frist subject:"))
b=int(input("Enter the second subject:"))
c=int(input("Enter the third subject:"))
d=int(input("Enter the fourth number:"))
e=int(input("Enter the fifth subject:"))
sum=a+b+c+d+e
avg=(sum/5)
per=(sum*100)/500
print("total marks is",sum)
print("average marks is",avg)
print("percentage will be",per)
if(per>=70 and per <=80):
       print("grade A")
elif(per>=60 and per<=70):
      print("grade B")
elif(per>=50 and per<=60):
       print("grade C")
elif(per>=40 and  per<=50):
     print("grade D")
elif(per==35):
  print("pass class")   
else:
     print("invalid result")


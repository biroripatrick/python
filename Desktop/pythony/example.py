
# x=10
# y="patrick"
# z=True
# m=("momo","hoho","jojo")
# j=["koko","hujokl","uiuiuiuu"]
# h={name:"patrick",age:67}

# print(j(2))
# fname = input("Input your First Name : ")
# lname = input("Input your Last Name : ")
# age = input("Input your age: ")
# print ("my name is: " + fname + " " + lname  +" " + age)

#The values in dictionary items can be of any data type a colling of dictionary
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

# print(thisdict)

#Print all key names in the dictionary, one by one
# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict:
#   print(thisdict[x])


#You can use the keys() method to return the keys of a dictionary:

#   thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)





#Adding an item to the dictionary is done by using a new index key and assigning a value to it:

# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict["color"] = "red"
# print(thisdict)

#The update() method will update the dictionary with the 
#items from a given argument. If the item does not exist, the item will be added.

# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.update({"color": "red"})


#There are several methods to remove items from a dictionary
#The pop() method removes the item with the specified key name:
# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# thisdict.pop("model")
# print(thisdict)


#QUESTION 2



# x= int(input("Enter first number:"))
# y= int(input("Enter second number:"))
# sum=x+y
# average=sum/2
# print("Sum of the given two numbers is:", sum)
# print("Average of the given numbers is:", average)

# def total(a,b):
#    sum=a+b
#    print(" Sum of ",a,"and"," sum of ",b,sum )  
# a= int(input("Enter first number:"))
# b= int(input("Enter second number:"))
# total(a,b)


# from math import pi
# r = float(input ("Input the radius of the circle : "))
# print ("The area of the circle with radius " + str(r) + str(pi * r**2))


# class calculator:
#     def add(self,num1,num2):
#       return num1+num2

#     def substract(self,num1,num2):
#       return num1-num2

#     def multiply(self,num1,num2):
#       return num1*num2

#     def devide(self,num1,num2):
#       return num1/num2

# calc=calculator()

# print("enter number your choice\n")
# print("1. for add\n")
# print("2. for substract \n")
# print("3. for multiply\n")
# print("4. for devide\n")
# choice=int(input(""))

# num1=int(input("enter the number 1:"))
# num2=int(input("enter the number 2:"))



# if(choice==1):
#   sum=calc.add(int(num1),int(num2))
#   print("sum is :"+str(sum))
# elif(choice==2):
#   print("difference is :"+str(calc.substract(float(num1),float(num2))))
# elif(choice==3):
#   print("product is :"+str(calc.multiply(float(num1),float(num2))))
# elif(choice==4):
#   print("ratio is :"+str(calc.devide(float(num2),float(num2))))




# numbers = [    
#     386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
#     399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
#     815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
#     958,743, 527
#     ]

# for x in numbers:
#     if x == 237:
#         print(x)
#         break;
#     elif x % 2 == 0:
#         print(x)
# b = int(input("enter  the base : "))
# h = int(input("enter the height : "))

# area = b*h/2

# print("area of triangle is = ", area)

# for fizzbuzz in range(51):
#     if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#         print("fizzbuzz")
#         continue
#     elif fizzbuzz % 3 == 0:
#         print("fizz")
#         continue
#     elif fizzbuzz % 5 == 0:
#         print("buzz")
#         continue
#     print(fizzbuzz)
# n = int(input("Input a number: "))

# # use for loop to iterate 10 times
# for i in range(1,11):
#    print(n,'x',i,'=',n*i)



# marks = float(input("Enter your marks in Computer Science: "))
# if marks > 90:
#     print("Grade: O")
# elif marks >= 80 and marks < 90:
#     print("Grade: A+")
# elif marks >= 70 and marks < 80:
#     print("Grade: A")
# elif marks >= 60 and marks < 70:
#     print("Grade: B+")
# elif marks >= 50 and marks < 60:
#     print("Grade: B")
# elif marks >= 40 and marks < 50:
#     print("Grade: C")
# else:
#     print("Grade: F")


#include <stdio.h>
# int main(void){
# int num;
# printf("Enter your mark ");
# scanf("%d",&num);
# printf(" You entered %d", num); // printing outputs
# 	if (num>100) printf(" ! Wrong data ");
# 	else if(num >= 80){
# 	printf(" You got A grade"); // printing outputs
# 		}
# 	else if ( num >=60){ // Note the space between else & if
# 		printf(" You got B grade");
# 		}
# 	else if ( num >=40){
# 		printf(" You got C grade");
# 		}
# 	else if ( num < 40){
# 		printf(" You Failed in this exam");
# 		}
# return 0;
# }


# marks=float(input("enter marks here"))
# if marks > 80:
#   print(" grade: distination")
# elif marks >= 70 and marks <= 79:
#   print("Excellent")
# elif marks >= 60 and marks <= 69:
#   print("Good")
# elif markss <  50 and marks >= 59:
#   print("failed")


# english = float(input(" Please enter English Marks: "))
# math = float(input(" Please enter Math score: "))
# computers = float(input(" Please enter Computer Marks: "))
# physics = float(input(" Please enter Physics Marks: "))
# chemistry = float(input(" Please enter Chemistry Marks: "))

# total = english + math + computers + physics + chemistry
# percentage = (total / 500) * 100
# print("Total Marks = %.2f"  %total)
# print("Marks Percentage = %.2f"  %percentage)

# if(percentage >= 90):
#   print("A Grade")
# elif(percentage >= 80):
#   print("B Grade")
# elif(percentage >= 70):
#   print("C Grade")
# elif(percentage >= 60):
#   print("D Grade")
# elif(percentage >= 40):
#   print("E Grade")
# else:
#   print("Fail")

  # number = int(input(" Please Enter any Integer Value : "))
  # if(number % 2 == 0):
  #   print("{0} is an Even Number".format(number))
  #   else:
  #     print("{0} is an Odd Number".format(number))



# Python Program to Calculate Electricity Bill
 
units = int(input(" Please enter Number of Units you Consumed : "))
if(units > 500):
amount = units * 9.65
surcharge = 85
elif(units >= 300):
amount = units * 7.75
surcharge = 75
elif(units >= 200):
amount = units * 5.26
surcharge = 55
elif(units >= 100):
amount = units * 3.76
surcharge = 35
else:
amount = units * 2.25
surcharge = 25
total = amount + surcharge
print("\nElectricity Bill = %.2f"  %total
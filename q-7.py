#....Write a python program to check whether a year is leap year or not.


a = int(input("enter year:"))
if a % 4 == 0:
  print("leap year.")
else:
  print("not a leap year.")

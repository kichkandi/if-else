#..Write a python program to find a maximum between three numbers.

a = int(input("enter the num:"))
b = int(input("enter the second num:"))
c = int(input("enter the third num:"))
if a>b and a>c:
  print("a is maximum num")
elif b>a and b>c:
  print("b is maximum num")
else:
  print("c is maximum num")
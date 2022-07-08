#..Write a python program to find a maximum between three numbers.

 a = int(input("enter the num:"))
b = int(input("enter the second num:"))
c = int(input("enter the third num:"))
if a<b and a<c:
  print("a is maximum num")
elif b>a and b>c:
  print("b is maximum num")
elif c>a and c>b:
  print("c is maximum num")
elif a==b and b==c:
  print("both are equal")
elif a==b and b>c:
  print("a and b both are maximum num")
elif a==c and c>b:
  print("a and c both are maximum num")
else:
  print("b and c both are maximum num")

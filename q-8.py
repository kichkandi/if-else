#.....Write a python program to check whether a character is an alphabet or not.


s = input("enter a character:")
if s>="a" and s<="z" or s>="A" and s<="Z":
  print("alphabet")
elif s>="0" and s<="9":
  print("number")
else:
  print("special character")

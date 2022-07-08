#.....Write a python program to check whether a character is an alphabet or not.


s = input("enter the character:")
if s=="a" or s=="e" or s=="i" or s=="o" or s=="u" or s=="A" or s=="E" or s=="I" or s=="O" or s=="U":
  print("it is a vowel")
elif s>="0" and s<="9":
  print("please enter the alphabet")
else:
  print("consonent")

  
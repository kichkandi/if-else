#.....Write a python program to input any alphabet and check whether it is vowel or consonant.



s = input("enter the character:")
if s=="a" or s=="e" or s=="i" or s=="o" or s=="u" or s=="A" or s=="E" or s=="I" or s=="O" or s=="U":
  print("it is a vowel")
elif s>="0" and s<="9":
  print("please enter the alphabet")
else:
  print("consonent")




longstring = "jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi"
 
vowel1 = longstring.rfind("a")
print(vowel1)
vowel2 = longstring.rfind("e")
print(vowel2)
vowel3 = longstring.rfind("i")
print(vowel3)
vowel4 = longstring.rfind("o")
print(vowel4)
vowel5 = longstring.rfind("u")
print(vowel5)
vowel6 = longstring.rfind("y")
print(vowel6)

print("\n") 

if (vowel1 > vowel2) or (vowel1 > vowel3) or (vowel1 > vowel4) or (vowel1 >vowel5) or (vowel1 >vowel6):
    print(vowel1)

elif (vowel2 > vowel1) or (vowel2 > vowel3) or (vowel2 > vowel4) or (vowel2 >vowel5) or (vowel2 > vowel6):
    print(vowel1)

elif (vowel3 > vowel2) or (vowel3 > vowel1) or (vowel3 > vowel4) or (vowel3 >vowel5) or (vowel3 > vowel6):
    print(vowel3)

elif (vowel4 > vowel2) or (vowel4 > vowel3) or (vowel4 > vowel1) or (vowel4 >vowel5) or (vowel4 >vowel6):
    print(vowel4)

elif (vowel5 > vowel2) or (vowel5 > vowel3) or (vowel5 > vowel4) or (vowel5 >vowel1) or (vowel5 >vowel6):
    print(vowel5)

elif (vowel6 > vowel2) or (vowel6 > vowel3) or (vowel6 > vowel4) or (vowel6 >vowel5) or (vowel6 >vowel1):
    print(vowel6)

else :
    print("God knows!")
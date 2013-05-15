# FizzBuzz is a game that has gained in popularity as a programming assignment to weed out non-programmers during job interviews. The object of the assignment is less about solving it correctly according to the below rules and more about showing the programmer understands basic, necessary tools such as if-/else-statements and loops.

#The rules of FizzBuzz are as follows:
#For numbers 1 through 100,
# if the number is divisible by 3 print Fizz;
# if the number is divisilbe by 5 print Buzz;
# if the number is divisible by 3 and 5 (15) print FizzBuzz;
# else, print the number.


# 0. Too literal
#
#for n in range(1,101):
#  if n%3==0: print("Fizz")
#  if n%5==0: print("Buzz")
#	if n%15==0: print("FizzBuzz")
#	else: print(n)

# 1. Inelegant
#
#for n in range(1,101):
#    if n%15==0:
#        print("FizzBuzz")
#    elif n%3==0:
#        print("Fizz")
#    elif n%5==0:
#        print("Buzz")
#    else:
#        print(n)

# 2. List comprehension
# FB = [f+b for f, b in zip(33*["","","Fizz"]+[""], 20*["","","","","Buzz"])]
# for n in range(100):
#    if FB[n]=="": print(n+1)
#    else: print(FB[n])

# 3. One line!
# print("\n".join([max(f+b,str(n+1)) for f,b,n in zip(33*["","","Fizz"]+[""], 20*["","","","","Buzz"],range(100))]))

# 4. One line, more generalized, as a function:
fizzbuzz = lambda f, b, num: [max(fi+bi,str(i)) for fi, bi, i in zip((num//f+1)*((f-1)*[""]+["Fizz"]), (num//b+1)*((b-1)*[""]+["Buzz"]),range(1,num+1))]

# Then format as a string:
print " ".join(fizzbuzz(3,5,100))
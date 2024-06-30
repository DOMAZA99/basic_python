"""
#
# Part: Python Conditions                                #Conditions 
#
"""

a = 200
b = 500
if a > b:
    print("a > b is True.")
elif a < b:
    print("a < b is True1.")
elif a <= b:
    print("a < b is True2.")
elif a == b:
    print("a < b is True3.")
else:
    print("Nothing.")

if a < b: print("a < b is True.")

print("B") if a < b else print("A")

a = 200
b = 30
c = 500
if (a > b) and (c > a):
    print("Both is True.")
if a > b or a > c:
    print("some cond is True.")
if not a > b:
    print("not")
if b >a:
    print("pass")
    pass

x = 19
if x > 10:
    print("Let's go!")
if x > 20:
    print("x > 20 is Ture1")
if x > 20:
    print("x > 20 is Ture2")
if x > 20:
    print("x > 20 is Ture3")
else:
    print("x > 20 is False")


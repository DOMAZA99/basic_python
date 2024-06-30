# This is a comment
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = ระยะเวลา (s)
print("---------------------------")
print("Hello World 1")

"""
# This is a comment
# v = s/t
# v = ความเร็ว (m/s)
# s = ระยะทาง (m)
# t = ระยะเวลา (s)
"""
print("---------------------------")
print("Hello World 2")

print("---------------------------")

"""
#
# Part : Python Variables ********
#
"""

x = 5
y = "Hey Bro"
print(x, y)

x = str(3)
y = int(3)
z = float(3)
print(type(x), type(y), type(z))

print("                           ")
print("---------------------------")

"""
#
# Part : Variables Names ********
#
"""

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
MY_VAR = "John"
myvar2 = "John"

# CameL Case
myVariableName = "John"
# PascaL Case
MyVariableName = "John"
# Snake Case
my_variable_name = "John"

"""
#
# Part : Python String ********
#
"""

#----------------------------------
x = "Hey Bro"
print(x)
print("                           ")
#----------------------------------
y = """1 Hey Bro
2 Hey Bro
3 Hey Bro
4 Hey Bro
5 Hey Bro"""
print(y)
print("                           ")
#----------------------------------
x = "Hey Bro"
print(x[4])                                         #เจาะจงคำ
print(len(x))                                       #เช็คจำนวน
print("                           ")

print("Hey " in x)
print("What Sup" not in x)
print(x.upper())                                    #ตัวพิมพ์ใหญ่
print(x.lower())                                    #คัวพิมพ์เล็ก
print(x.replace("Bro", "Sur"))                      #replace แทนค่า
print(x.split(" "))                                 #แบ่งคำมาทั้ง 2

a = "Apple"
b = "Banan"
print(a + " " + b)                                  #ต่อคำ

price = 20
word = f"Price : {price:.2f}"
print(word)                                         #โชว์จำนวน 2 ทศนิยม






print("                           ")
print("---------------------------")

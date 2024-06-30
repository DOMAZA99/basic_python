"""
#
# Part: Python Function                                #สารถเรียกใช้งานชุดโค๊ดซ้ำๆได้
#
"""

def my_function():                                  #สร้าง Function
    print("Hello World 1")
    print("Hello World 2")

my_function()                                       #เรียกใช้ Function โดยพิมพ์ my_function
my_function()

def my_name(fname):
    print("my name is ", fname)

my_name("Anya")

def my_name2(fname , Lname):
    print("my name is ", fname, Lname)

my_name2("Anya", "Roger")
my_name2(Lname = "Roger", fname = "Anya")

def my_name3(Lname = "Roger"):                  #เป็นการกำหนดค่า เริ่มต้นให้กับ function
    print("My Last name is ", Lname)

my_name3()
my_name3("Paul")

def my_friuts(fruits):
    for fruit in fruits:
        print(fruit)

fruit = ["apple", "banana", "coconut"]
my_friuts(fruit)

def red_potion(hp):
    return hp + 50

print("HP: ", red_potion(100))
print("HP: ", red_potion(70))

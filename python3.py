"""
#
# Part : Python Collections
# List, Tuple, Set and Dictionary
# 
"""

"""
#
# Part : Python List
# 
"""

this_list = ["apple", "banana", "coconute", "apple", "banana"]
print(this_list)                                                    #ใช้แสดงข้อมูลทั้งหมดในตัวแปร
print(type(this_list))                                              #ใช้กำหนดประเภท
print(len(this_list))                                               #เช็คจำนวนในตัวแปรว่ามีขออยู่เท่าไหร่
print(this_list[0])                                                 #[] ใช้หาตำแหน่ง แต่ล่ะตำแหน่งจะเริ่มต้นจาก 0
this_list.append("cherry")                                          #ใช้สำหรับเพิ่มตัวแปรเข้าไปใน this_list
print(this_list, len(this_list))                                    #ใช้แสดงข้อมูลทั้งหมดในตัวแปร และเช็คจำนวนในตัวแปรว่ามีขออยู่เท่าไหร่
this_list.insert(1, "orange")                                       #insert ใช้สำหรับแทรกตัวแปร และระบุตำแหน่ง
print(this_list, len(this_list))                                    #len ใช้นับจำนวน

print("--------------this_list2-3 ---------------")
this_list2 = ["apple", "banana", "coconute", "apple", "banana"]
this_list3 = ["mango", "pineapple", "grape"]
this_list2.extend(this_list3)                                       #extend ใช้สำหรับนำตัวแปรมาต่อกัน
print(this_list2, len(this_list2))

print("--------------this_list4---------------")
this_list4 = ["apple", "banana", "coconute", "apple", "banana"]
this_list4.remove("banana")                                         #remove ใช้สำหรับลบข้อมูลในตัวแปร จะลบข้อมูลในตัวแปรลำดับต้นๆ
print(this_list4, len(this_list4))

print("--------------this_list5---------------")
this_list5 = ["apple", "banana", "coconute", "apple", "banana"]
this_list5.pop(0)                                                   #pop ใช้สำหรับลบตามตำแหน่ง เริ่มต้นจาก 0
print(this_list5, len(this_list5))

print("--------------this_list6---------------")
this_list6 = ["apple", "banana", "coconute", "apple", "banana"]
del this_list6[1]                                                   #del ลบข้อมูลแต่ยังจอง Ram ไว้อยู่
print(this_list6, len(this_list6))

this_list6.clear()                                                  #clear ลบข้อมูลทั้งหมด แต่ตัวแปรยังอยู่
print(this_list6, len(this_list6))

del this_list5                                                      #ลบทั้งหมด
#print(this_list5, len(this_list5))

this_list7 = ["apple", "banana", "coconute", "apple", "banana"]
this_list7.sort()                                                   #sort เรียงลำดับตามตัวอักษรหน้าไปหลัง
print(this_list7, len(this_list7))

this_list8 = ["apple", "banana", "coconute", "apple", "banana"]
this_list8.reverse()                                                #เรียงลำดับจากหลังมาหน้า
print(this_list8, len(this_list8))

list1 = ["a", "b", "c"]
list2 = [1, 2, 3 ]
list3 = list1 + list2
print(list3)

"""
#
#  Prat: pythom Tuple                                                #เรียงลำดับให้ และไม่สามรถเปลี่ยนแปลงค่าได้
#
"""
this_tuple = ("apple", "banana", "coconute")
print(this_tuple)
print(type(this_tuple))                                             #ใช้แสดงประเภท Class
print(len(this_tuple))
print(this_tuple[2])

this_tuple2 = ("apple", "banana", "coconute")
this_tuple3_list = list(this_tuple2)
print(this_tuple3_list)
print(type(this_tuple3_list))
this_tuple4 = tuple(this_tuple3_list)
print(this_tuple4)
print(type(this_tuple4))

this_tuple5 = ("apple", "banana", "coconute")
this_tuple6_list = list(this_tuple5)
this_tuple6_list.append("mango")                        #เพิ่มตัวแปรใช้คำสั่ง .append
this_tuple7 = tuple(this_tuple6_list)
print(this_tuple7)
print(type(this_tuple7))

this_tuple8 = ("apple", "banana", "coconute")
this_tuple9_list = list(this_tuple8)
this_tuple9_list.remove("banana")                       #ลบตัวแปรใช้คำสั่ง .remove
this_tuple10 = tuple(this_tuple9_list)
print(this_tuple10)
print(type(this_tuple10))

del this_tuple10
# print(this_tuple10)

tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3= tuple1 + tuple2                            #tuple สามารถนำมา + - กันได้ /โดยไม่ต้องแปลงเป็น list
print(tuple3)

"""
#
# part: python Set                              # ใช้สำหรับเก็บค่าและนำกลับมาใช้
# 
"""

this_set = {"apple", "banana","coconut"}
print (this_set)
print(type(this_set))
print(len(this_set))

for X in this_set:                              # for ใช้สำหรับวนลูปจนกว่าค่าจะครบ
    print(X)
print("banana" in this_set)

this_set2 = {"apple", "banana","coconut"}          #this_set ไม่สามารถแก้ไขได้ แต่สามารถ เพิ่ม หรือ ลบ ตัวแปรได้
this_set2.add("orange")                            #add ใช้เพิ่มข้อมูลตัวแปร
print(this_set2, len(this_set2))
this_set2.remove("apple")
print(this_set2, len(this_set2))

this_set3 = {"apple", "banana","coconut"} 
this_set4 = {"pineapple", "grape"} 
this_set3.update(this_set4)                         #.update ใช้สำหรับต่อค่า
print(this_set3, len(this_set3))

this_set5 = {"apple", "banana","coconut"} 
this_set6 = {"pineapple", "grape"}
this_set7 = {1, 2, 3}
this_set8 = this_set5 | this_set6 | this_set7           #| คือการยูเนี่ยน คือ เอาค่าทั้งหมดมาต่อกัน
print(this_set8, len(this_set8))

this_set8.clear()                                        #set สามารถ เคลียได้ แลพ del หรือ ลบได้
print(this_set8, len(this_set8))
del this_set8
#print(this_set8, len(this_set8))

"""
#
# Part: Python Dictionry                                #Dictionry สามารถตั้งชื่อ / ตำแหน่งindex ได้ แต่ไม่สามารถซ้ำกันได้
#
"""
this_dict = {
    "brand": "Ford",
    "model": "Raptor",
    "year": "2023"
}
print(this_dict)
print(type(this_dict))
print(len(this_dict))
print(this_dict["brand"])
print(this_dict.get("year"))                            #.getใช้เข้าถึงค่าของตัวแปร
print(this_dict.keys())                                 #.keyใช้สำหรับเข้าถึงตัวแปร

this_dict["year"] = 2020
print(this_dict)
this_dict.update({"year": 2021})
print(this_dict)

this_dict["color"] = "red"
print(this_dict)

del this_dict["year"]
print(this_dict)

this_dict.clear()
print(this_dict, len(this_dict))
del this_dict
#print(this_dict)

this_dict2 = {
    "brand": "Ford",
    "model": "Raptor",
    "year": "2023"
}
this_dict3 = {
    "brand": "Honda",
    "model": "Civic",
    "year": "2019"
}
this_dict4 = {
    "brand": "Toyota",
    "model": "Colora",
    "year": "2017"
}
my_car= {
    "car1": this_dict2,
    "car2": this_dict3,
    "car3": this_dict4
}
print(my_car, len(my_car))
print(my_car["car2"]["model"])

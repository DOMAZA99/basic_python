"""
#
# Part: Python While Loop                                #วนลูปได้หลายตัวแปร
#
"""
i = 1                                               # แทนค่า i = 1
while i < 5:                                        # ถ้า i=1 น้อยกว่า 5
    print("i = ", i)                                # ให้แสดง i = 1
    i+=1                                            # i=1 + 1 
                                                    # ทำวนไป i = 1+1 น้อยกว่า 5 มั้ย ทำไปเรื่อยๆกัน i ไม่น้อยกว่า 5

i = 1
while i < 5:
    print("i = ", i)
    if i == 3:
        break                           #เมื่อได้จำนวนแล้ว ก็จะหยุด ด้วย break
    i+=1


# i = 1             
# while i < 5:
#    print("i = ", 1)
#    if i == 3:
#    continue                      #ทำต่อไปเรื่อยๆ ด้วย continue
#    i+=1


i = 1
while i < 5:
    print("i = ", i)
    i += 1
else:
    print("Game Over")

"""
#
# Part: Python For Loop                                #For วนในตำแหน่งที่ 0 และ 1 และ 2 วนไปเรื่อยๆจนกว่าจะหมด หรือ แสดงในตำแหน่งที่ 0 จนครบ
#
"""
fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    print("fruit: ", fruit)

for fruit in fruits:
    print("fruit: ", fruit)
    if fruit == "banana":
        break

for fruit in fruits:
    if fruit == "banana":
        break
    print("fruit: ", fruit)

for fruit in fruits:
    if fruit == "banana":
        continue                                    #continue ใน For จะเป็นการข้าม ในลูปนั้น ซึ่งแตกต่างจาก While
    print("fruit: ", fruit)

for x in range(len(fruits) + 1):
    print("Number = ", x)

for x in range(5):
    print("Number = ", x)
else:
    print("Game Over")

adjs = ["Red", "Yellow", "Brown"]
fruits = ["apple", "banana", "coconut"]
for adj in adjs:
    for fruit in fruits:
        print(adj, fruit)
        
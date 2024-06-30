odd_numbers = []
even_numbers = []

                                                    # วนลูปผ่านเลขตั้งแต่ 1 ถึง 20
for x in range(1, 21):
                                                    # ตรวจสอบว่าเลขนั้นเป็นเลขคี่หรือเลขคู่โดยใช้ 2 หาร
    if x % 2 == 0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

                                                        # ให้แสดงเลขคี่และเลขคู่
print("เลขคี่:", odd_numbers)
print("เลขคู่:", even_numbers)
                                                                        
                                                                        #นายภาณุสมใจ 
                                                                        #รหัส 6749010014 ทล.บ.67-1
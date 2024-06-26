#1-8: Operator Precedence
#แบบฝึกหัด 1-8 ข้อที่ 1
#สั่ง Run โปรแกรมข้างล่างนี้ แล้วพยายามทำความเข้าใจว่า ทำไมถึงได้ผลลัพธ์ดังที่แสดง
print("2+3*4 =", 2+3*4)
print("(2+3)*4 =", (2+3)*4)
print("2+3*4//2%4-1 =", 2+3*4//2%4-1)
print("6/2*3 =", 6/2*3)
print("6/(2*3) =", 6/(2*3))
print("2**3**2 =", 2**3**2)
print("(2**3)**2 =", (2**3)**2)
print("-2*-4 =", -2*-4)
print("-2**4 =", -2**4)
print("(-2)**4 =", (-2)**4)

#แบบฝึกหัด 1-8 ข้อที่ 2
#อยากทราบว่า นับจากเวลาบ่ายโมง 13:00:00 ไปอีก 98789 วินาที จะเป็นเวลาอะไร ให้เขียนคำสั่งคำนวณและแสดงผล ในรูปแบบ HH:MM:SS
h = 13
m = 0
s = 0

t = h*3600 + m*60 + s
t += 98789
h = t//3600 % 24
m = t % 3600 // 60
s = t % 60
print(str(h)+":"+str(m)+":"+str(s))

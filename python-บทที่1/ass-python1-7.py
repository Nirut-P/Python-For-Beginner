#1-7: Math Module and Function
#แบบฝึกหัด 1-7 ข้อที่ 1
# อ่านจำนวนเต็มจาก input มาเก็บใน m
# อ่านจำนวนเต็มจาก input มาเก็บใน k
# นำค่าใน k ไปเพื่มให้กับตัวแปร m

# อ่านสตริงจาก input เก็บใน s
# อ่านสตริงจาก input เก็บใน t
# นำสตริงใน t ไปต่อทางขวาของ s

# อ่านจำนวนจริงจาก input มาเก็บใน d
#    d เป็นมุม หน่วยเป็นองศา
# ให้ r เก็บค่ามุมหน่วยเรเดียนที่แปลงจาก d
# ให้ x เก็บค่า sin( r )
# ให้ y เก็บค่าเดียวกับ x 
#    แต่ปัดเศษให้มีเลขหลังจุดทศนิยม 2 ตำแหน่ง

import math

m = int(input())
k = int(input())
m += k
s = input()
t = input()
s += t
d = float(input())
r = math.radians(d)
x = math.sin(r)
y = round(x, 2)
print (r)
print (x)
print (y)
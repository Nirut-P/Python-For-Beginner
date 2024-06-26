#4-4: for i in range
#แบบฝึกหัด 4-4 ข้อที่ 1
#เขียนโปรแกรมตามผังงาน
n = int(input())
s = 0
for i in range(n):
    s += i
print(s)

#แบบฝึกหัด 4-4 ข้อที่ 2
#เขียนโปรแกรมตามผังงาน
n = int(input())
s = 0
for i in range(1,n+1):
    if i%2 == 0:
        s += i
    s += i
print(s)

#แบบฝึกหัด 4-4 ข้อที่ 3
#เขียนโปรแกรมตามผังงาน
n = int(input())
s = 0
k = 1
for i in range(n,0,-1):
    if i%2 == 0:
        s += i*k
    else:
        s -= k
    k += 2
    s += i*k
print(s)

#แบบฝึกหัด 4-4 ข้อที่ 4
#อ่านจำนวนเต็ม a, b และ c จาก input แล้วแสดงจำนวนเต็มที่มีค่า a, a+c, a+2c, ... บรรทัดละหนึ่งค่า 
#โดยจะหยุดแสดงเมื่อค่าที่คำนวณมากกว่าหรือเท่ากับ b เช่น a=2, b=7, c=2 จะแสดง 2, 4 และ 6 บรรทัดละค่า
x = input().split()
a = int(x[0])
b = int(x[1])
c = int(x[2])
for i in range(a, b, c):
    print(i)


#แบบฝึกหัด 4-4 ข้อที่ 5
#อ่านจำนวนเต็มไม่ติดลบ m จาก input แล้วแสดงจำนวนเต็มที่มีค่าตั้งแต่ -m จนถึง m บรรทัดละหนึ่งค่า
m = int(input())
for i in range(-m, m+1):
    print(i)

#แบบฝึกหัด 4-4 ข้อที่ 6
#อ่านจำนวนเต็มไม่ติดลบ m จาก input แล้วแสดงเฉพาะจำนวนเต็มคู่ที่มีค่าตั้งแต่ -m จนถึง m บรรทัดละหนึ่งค่า
m = int(input())
s = -m; t = m
if m%2 == 1: 
    s += 1
    t -= 1
for i in range(s, t+1, 2):
    print(i)

#แบบฝึกหัด 4-4 ข้อที่ 7
#อ่านจำนวนเต็ม n จาก input แล้วเขียนคำสั่งเพื่อคำนวณและแสดงค่าของ ∑^ni=1i^5 (โดยใช้วงวน for)
n = int(input())
s = 0
for i in range(1,n+1):
  s += i**5
print(s)


#แบบฝึกหัด 4-4 ข้อที่ 8
#ข้อมูลที่ input มีบรรทัดแรกเป็นจำนวนเต็ม n ตามด้วยอีก n บรรทัดเป็นจำนวนเต็ม d0, d1, ..., dn-1 บรรทัดละจำนวน จงเขียนโปรแกรมอ่านข้อมูลจาก input (โดยใช้วงวน for) เพื่อหาผลรวมของ d0, d1, ..., dn-1
n = int(input())
s = 0
for k in range(n):
    s += int(input())
print(s)


#แบบฝึกหัด 4-4 ข้อที่ 9
#มีรายการของจำนวนเต็มในบรรทัดเดียวกันของ input เช่น 10 20 30 55 จงเขียนชุดคำสั่งอ่านจำนวนเต็มเหล่านี้เก็บใส่ตัวแปรชื่อ a ที่เป็นลิสต์ 
#จากนั้นสร้างลิสต์ของจำนวนจริงมีขนาดเท่ากับของ a แต่ละช่องเก็บค่าครึ่งหนึ่งของที่เก็บใน a เช่น อ่านข้อมูลได้ a = [10,20,30,55] 
#แล้วก็สร้าง b = [5.0, 10.0, 15.0, 27.5]
x = input().split()
a = [0]*len(x)
for i in range(len(x)):
    a[i] = int(x[i])
b = [0.0]*len(x)
for i in range(len(a)):
    b[i] = a[i]/2

#แบบฝึกหัด 4-4 ข้อที่ 10
#อ่านจำนวนเต็ม n จาก input แล้วแสดงรูปสามเหลี่ยมดังตัวอย่าง
n = int(input())
for i in range(1,n+1):
    print("*"*i)

#แบบฝึกหัด 4-4 ข้อที่ 11
#อ่านจำนวนเต็ม n จาก input แล้วแสดงรูปสามเหลี่ยมดังตัวอย่าง
n = int(input())
for i in range(1,n+1):
    print("*"*i)
for i in range(n-1,0,-1):
    print("*"*i)

#แบบฝึกหัด 4-4 ข้อที่ 12
#อ่านจำนวนเต็ม n จาก input แล้วแสดงรูปสามเหลี่ยมดังตัวอย่าง
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i) + "*"*i)

#แบบฝึกหัด 4-4 ข้อที่ 13
#อ่านสตริง t จาก input เพื่อนับและแสดงว่ามีสระใน t กี่ตัว (นับทั้งตัวเล็กและตัวใหญ่ โดยใช้วงวน for) เช่น Anna มีสระเป็นจำนวน 2 ตัว แบบฝึกหัดของบทก่อน 
#เราเขียนโดยใช้วงวน while ดังแสดงข้างล่างนี้
t = input()
c = 0
vowels = "aeiouAEIOU"
for k in range(len(t)):
    if t[k] in vowels:
        c += 1
print(c)


#แบบฝึกหัด 4-4 ข้อที่ 14
#อ่านสตริง t จาก input แล้วนับและแสดงว่ามีสตริงย่อย "ABC" อยู่ภายในกี่ตำแหน่ง เช่น "ABCabcAABCABAABC" มี "ABC" อยู่ 3 ตำแหน่ง
t = input()
c = 0
for i in range(len(t)-2):
    if t[i:i+3] == "ABC":
        c += 1
print(c)

#แบบฝึกหัด 4-4 ข้อที่ 15
#อ่านสตริง t จาก input มาหนึ่งบรรทัด แล้วก็อ่านสตริง s จาก input อีกหนึ่งบรรทัด จากนั้นนับและแสดงว่า มีสตริงของ s อยู่ภายในสตริงของ t กี่ตำแหน่ง 
#เช่น t = "ABCabcAABCABAABC" และ s = "ABC" จะแสดง 3
t = input()
s = input()
c = 0
for i in range(len(t)-len(s)+1):
    if t[i:i+len(s)] == s:
        c += 1
print(c)

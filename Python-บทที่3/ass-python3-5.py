#3-5: if Statement
#แบบฝึกหัด 3-5 ข้อที่ 1
#เขียนโปรแกรมตามผังงานนี้
b = 1
if a < 0:
    a = -a
    b = 2*a
if not(a > 10):
    a *= 3
    b += a
print(a,b)

#แบบฝึกหัด 3-5 ข้อที่ 2
#เขียนโปรแกรมตามผังงานนี้
b = 1
if a < 0:
    a = -a
    b = 2*a
    if a > 10:
        a *= 3
        b += a
print(a,b)

#แบบฝึกหัด 3-5 ข้อที่ 3
#มีตัวแปร t เก็บสตริงอยู่แล้ว โดยที่ t มีตัวอักษรภายใน 5 ตัว จงแสดงจำนวนตัวใน t ที่เป็นสระ (นับทั้งตัวเล็กและตัวใหญ่) เช่น Annie มีสระ 3 ตัว
# ให้ c เก็บจำนวนสระ เริ่มต้นมีค่า 0
# ถ้าตัวที่ index 0 เป็นสระ ก็เพิ่ม c อีก 1
# แล้วก็ตรวจสอบตัวต่าง ๆ ที่เหลือ
c = 0
vowels = "aeiouAEIOU"
if t[0] in vowels:
    c += 1
if t[1] in vowels:
    c += 1
if t[2] in vowels:
    c += 1
if t[3] in vowels:
    c += 1
if t[4] in vowels:
    c += 1
print(c)

#แบบฝึกหัด 3-5 ข้อที่ 4
#มีตัวแปร text เก็บสตริงอยู่แล้ว อยากทราบว่าใน text มีตัวอักษรที่เป็นสระอะไรบ้าง (เฉพาะตัวเล็ก) เช่น Mission ให้แสดง io, understand ให้แสดง aeu (แสดงสระที่มี ตามลำดับตัวอักษร) ถ้าไม่มีสระเลยให้แสดง No vowels
r = ""
c = "a"
if c in text:
    r += c
c = "e"
if c in text:
    r += c
c = "i"
if c in text:
    r += c
c = "o"
if c in text:
    r += c
c = "u"
if c in text:
    r += c
if r == "":
    print("No vowels")
else:
    print(r)



#3-1: Flowchart & if-else
#แบบฝึกหัด 3-1 ข้อที่ 1
#เขียนโปรแกรมตามผังงาน

a = int(input())
b = int(input())
if a < b:
  min = a
  max = b
else:
  min = b
  max = a
print(min, max)

#แบบฝึกหัด 3-1 ข้อที่ 2
#เขียนโปรแกรมตามผังงาน (มีตัวแปร a และ b ให้แล้ว ไม่ต้องตั้งค่าหรือรับอินพุตใด ๆ)
if abs(a-b) > 2:
    a,b = b,a
else:
    a = b**2 + a
print(a,b)

#แบบฝึกหัด 3-1 ข้อที่ 3
#เขียนโปรแกรมตามผังงาน (มีตัวแปร a ให้แล้ว ไม่ต้องตั้งค่าหรือรับอินพุตใด ๆ)
if a%2 == 0:
    a *= 2
else:
    if a > 10:
        a //= 2
    else:
        a = 0
print(a)

#แบบฝึกหัด 3-1 ข้อที่ 4
#เขียนโปรแกรมตามผังงาน (มีตัวแปร a ให้แล้ว ไม่ต้องตั้งค่าหรือรับอินพุตใด ๆ)
if a%2 == 0:
    if a > 10:
        a //= 2
    else:
        a = 0
else:
    a *= 2
print(a)

#แบบฝึกหัด 3-1 ข้อที่ 5
#เขียนโปรแกรมตามผังงาน (มีตัวแปร a ให้แล้ว ไม่ต้องตั้งค่าหรือรับอินพุตใด ๆ)
if a%2 == 0:
    b = 2*a
    if a > 10:
        a //= 2
    else:
        b += a
    a += b
else:
    a *= 2
print(a,b)


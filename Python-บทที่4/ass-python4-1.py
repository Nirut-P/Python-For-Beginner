#4-1: Flowchart
#แบบฝึกหัด 4-1 ข้อที่ 1
#เขียนโปรแกรมตามผังงานนี้
c = 0
while n > 0:
    n //= 2
    c += 1
print(c)

#แบบฝึกหัด 4-1 ข้อที่ 2
#เขียนโปรแกรมตามผังงานนี้
n = len(b)
k = 0
d = 0
while k < n:
    d += 2**k*int(b[n-k-1])
    k += 1
print(d)

#แบบฝึกหัด 4-1 ข้อที่ 3
#เขียนโปรแกรมตามผังงานนี้
c = 0
while n>0:
    n = n-1
    if n%3 == 0:
        n = n-c
        c += 1
print(c)
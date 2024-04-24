#3-4: Membership Operator (in)
#แบบฝึกหัด 3-4 ข้อที่ 1
#มีตัวแปร text เก็บสตริงอยู่แล้ว ถ้าใน text มี Python หรือ python ปรากฏอยู่ให้แสดง Yes ไม่เช่นนั้นแสดง No
if "Python" in text or "python" in text:
    print("Yes")
else:
    print("No")

#แบบฝึกหัด 3-4 ข้อที่ 1
#มีตัวแปร month เก็บสตริงอยู่แล้ว ถ้า month เก็บชื่อเดือน ให้แสดง Yes ไม่เช่นนั้นก็แสดง No ชื่อเดือนมีดังนี้ January, February, March, April, May, June, July, August, September, October, November, December
t = ["January", "February", "March",
        "April", "May", "June", "July",
        "August", "September", "October",
        "November", "December"]
if month in t:
    print("Yes")
else:
    print("No")


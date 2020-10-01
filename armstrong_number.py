###3-digit Armstrong Number = 153 because 13 + 53 + 33 = 153.
###4-digit Armstrong Number = 1634 because 14 + 64 + 34 + 44 = 1634.

num = int(input("Enter the number: "))
size = len(str(num))
sum = 0
def isArmstrong(n):
    global sum
    global num
    global size
    if n < 10:
        sum += n ** size
        return num == sum
    else:
        sum += (n % 10) ** size
        return isArmstrong(n // 10)
if isArmstrong(num):
    print(str(num) + " is an Armstrong Number.")
else:
    print(str(num) + " is NOT an Armstrong Number.")

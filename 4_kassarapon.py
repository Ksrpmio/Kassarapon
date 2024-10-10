def arrange(a, b):
    result = []
    
    while a > 0 or b > 0:
        if len(result) >= 2 and result[-1] == result[-2]:  #อักษรเดียวกันซ้ำกันเกิน 2 ครั้งหรือไม่
            if result[-1] == 'A':
                if b > 0:
                    result.append('B')
                    b -= 1
                else:
                    return "Error: "
            else:
                if a > 0:
                    result.append('A')
                    a -= 1
                else:
                    return "Error: "
        else:
            if a >= b:  #ให้ใส่ A ก่อน
                if a > 0:
                    result.append('A')
                    a -= 1
            else:  #ให้ใส่ B ก่อน
                if b > 0:
                    result.append('B')
                    b -= 1

    return ''.join(result)

a = int(input("Enter number A: "))
b = int(input("Enter number B: "))

output = arrange(a, b)
print(output)
print("Kassarapon_Chayanant")

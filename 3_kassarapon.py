def pattern(size):
    for i in range(size):
        for j in range(size):
            if i == j or i + j == size - 1:
                print("*", end="")
            else:
                print("-", end="")
        print()

size = int(input("Enter size: "))

if size % 2 == 1:
    pattern(size)
else:
    print("Enter an odd number!!!")
    print("Kassarapon_Chayanant")

def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

n = int(input("Enter number: "))

fibo = fibonacci(n)
print("Fibonacci: ", ', '.join(map(str, fibo)))
print("Kassarapon_Chayanant")
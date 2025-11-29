n = int(input("Enter how many Fibonacci numbers you want: "))

a, b = 0, 1
print(a, b, end=" ")

for _ in range(n - 2):
    c = a + b
    print(c, end=" ")
    a, b = b, c

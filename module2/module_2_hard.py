n = int(input("Введите число от 3 до 20: "))
result = ""

for i in range(1, n):
    for j in range(i+1, n+1):
        x = i+j
        if n % x == 0:
            result += str(i) + str(j)

print(result)
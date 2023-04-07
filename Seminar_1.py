#Задача 2: Найдите сумму цифр трехзначного числа

#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0) 

number = int(input())

# цифры каждого числа
num3 = number % 10
num2 = (number // 10) % 10
num1 = number // 100

print(f"{number} -> {num1 + num2 + num3} ({num1} + {num2} + {num3})")


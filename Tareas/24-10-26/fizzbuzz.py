print("Fizzbuzz: multiplos de 3 Fizz; multiplos de 5 Buzz; si es multiplo de ambos FizzBuzz")

num = 1

while num <= 30:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

    num = num + 1

print("Fin")
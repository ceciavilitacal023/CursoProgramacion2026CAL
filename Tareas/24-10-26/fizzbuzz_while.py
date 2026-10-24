print("Fizzbuzz: multiplos de 3 Fizz; multiplos de 5 Buzz; si es multiplo de ambos FizzBuzz")

num = 1
fizz = 0
buzz = 0
fizzbuzz = 0

while num >= 1 and num <= 30:
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
        fizzbuzz = fizzbuzz + 1
    elif num % 3 == 0:
        print("Fizz")
        fizz = fizz + 1
    elif num % 5 == 0:
        print("Buzz")
        buzz = buzz + 1
    else:
        print(num)

    num = num + 1

print("Cantidad de Fizz:", fizz)
print("Cantidad de Buzz:", buzz)
print("Cantidad de FizzBuzz:", fizzbuzz)
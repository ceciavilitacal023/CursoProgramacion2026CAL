fizz = 0
buzz = 0
fizzbuzz = 0

for num in range(1, 31):
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

print("Cantidad de Fizz:", fizz)
print("Cantidad de Buzz:", buzz)
print("Cantidad de FizzBuzz:", fizzbuzz)
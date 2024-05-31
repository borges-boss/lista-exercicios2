def is_prime_number(number:int):
    if(number <= 1):
        return False
    
    for i in range(2,number):
        if number % i == 0:
             return False
 
        return True


numbers = [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]

primeNumbers = [num for num in numbers if is_prime_number(num)]

print(primeNumbers)
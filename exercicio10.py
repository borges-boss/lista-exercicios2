def is_prime_number(number:int):
    if number <= 1:
        return False
    
    if number == 2:
        return True

    for i in range(2,number):
        if number % i == 0:
             return False
 
        return True
    


print(is_prime_number(7))
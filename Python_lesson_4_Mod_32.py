# AI Porgamming with Python: Lesson 4 Control Flow, Module 30: Check for Prime Numers
## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor
for num in check_prime: # iterate through the check_prime list
    for index in range(2, num): # search for factors, iterating through range starting from 2 num-1, i.e. for num = 26 check for factors up to 26
        if (num % index) == 0: # prime number check, if mod is 0
            print("{} is NOT a prime number because {} is a factor of {}".format(num, index, num))
            break
        elif index == num -1: # keep checking until all possible factors if prime found print is a prime message
            print("{} IS a prime number".format(num))
        

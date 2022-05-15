def collatz(number):
    while number != 1:
        print(number)
        if number % 2 == 0: # if even number
            number = number // 2
        else: # if odd number
            number = 3 * number + 1
    print(number)

print("This program will print the Collatz Sequence. \n Please enter an integer: ", end='')

try:
    num = int(input())
except ValueError:
    print("Must enter and integer!")
    exit()

collatz(num)



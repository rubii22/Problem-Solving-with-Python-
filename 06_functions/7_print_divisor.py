# Problem Statement

# Write the helper function print_divisors(num), which takes in a number and prints all of its divisors (all the numbers from 1
# to num inclusive that num can be cleanly divided by (there is no remainder to the division). Don't forget to call your function in main()!

# Solution

def print_divisors(num):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)  

def main():
    num = int(input("Enter a number: "))  
    print("Divisors of", num, "are:")
    print_divisors(num) 

main()

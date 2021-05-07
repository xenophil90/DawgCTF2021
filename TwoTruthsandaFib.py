from pwn import *
import math

# Define functions to find out what numbers are Fibonacci numbers
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s*s == x

def isFibonacci(n):
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)

# Establish Socket Connection and print what the server tells us
r = remote('167.172.155.117', 6000)
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
print(r.recvline())
input_numbers = r.recvline().decode()

# Convert string to usable stuff
input_numbers_split = input_numbers.split(',')

num1 = int(input_numbers_split[0].replace('[', ''))
num2 = int(input_numbers_split[1])
num3 = int(input_numbers_split[2].replace(']', ''))

# Check if the numbers provided are fibonacci numbers
if (isFibonacci(num1) == True):
    fibonacci_number = num1
if (isFibonacci(num2) == True):
    fibonacci_number = num2
if (isFibonacci(num3) == True):
    fibonacci_number = num3

# Send the fibonacci number to the server
r.send(str(fibonacci_number)+"\n")

# Repeat...
while True:
    print(r.recvline())
    print(r.recvline())

    input_numbers = r.recvline().decode()
    input_numbers_split = input_numbers.split(',')

    num1 = int(input_numbers_split[0].replace('[', ''))
    num2 = int(input_numbers_split[1])
    num3 = int(input_numbers_split[2].replace(']', ''))

    if (isFibonacci(num1) == True):
        fibonacci_number = num1
    if (isFibonacci(num2) == True):
        fibonacci_number = num2
    if (isFibonacci(num3) == True):
        fibonacci_number = num3

    r.send(str(fibonacci_number)+"\n")

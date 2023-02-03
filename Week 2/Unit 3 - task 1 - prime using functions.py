# this part tells you if a number is prime
num = int(input("enter a number "))
while num < 2:
    print("Error")
    num = int(input("enter a number "))

def prime(num):
    if num > 1:
        for i in range(2, num//2):
            if (num % i) == 0:
                return "is not a prime number"
        else:
            return "is a prime number"

output = prime(num)
print(num, output, ",Here are all the primes up to ", num)

# this prints all the numbers up to that number
def primeRange(num):
    if num < 2:
        raise ValueError("There is no prime number under 2")
    else:
        for Loop in range(2, num+1):
            for i in range(2, Loop):
                if (Loop % i) == 0:
                    break
            else:
                print(Loop)

primeRange(num)
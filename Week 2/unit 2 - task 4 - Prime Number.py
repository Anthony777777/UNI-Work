n = int(input("enter a number: "))

if (n < 2):
    print("please enter a number over 2.")
else:
    print("the prime numbers up to the entered number are ")
    for i in range(n + 1):
        if i > 2:
            # Assume number is prime unless proven otherwise
            prime = True
            # Start at 2 because everything is divisible by 1
            count = 2
            while count < i and prime == True:
                # Check if there's no remainder (not prime)
                if (i % count) == 0:
                    prime = False
                else:
                    count += 1
            if prime == True:
                print(i)
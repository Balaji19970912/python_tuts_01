prime_number = 26
count = 0

if(prime_number > 1):
    for i in range(2, prime_number+1):
        if(prime_number % i == 0):
            count += 1

if(count > 1):
    print("Number is not prime!")
else:
    print("Number is prime!")
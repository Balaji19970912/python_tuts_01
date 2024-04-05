range_of_numbers = 10
sum_of_even_numbers = 0

for i in range(0,range_of_numbers+1):
    if(i%2 == 0):
        sum_of_even_numbers += i

print("Sum of even numbers =", sum_of_even_numbers)
def fact_number(num):
    if(num == 1):
        return 1
    return num * fact_number(num-1)

fact_find_num = 5
fact_res = fact_number(fact_find_num)

print("Factorial of",fact_find_num,"is =",fact_res)
fact_number = 10
fact_res = 1
temp = fact_number

while(fact_number > 0):
  fact_res *= fact_number
  fact_number -= 1

print("Factorial of",temp,"is =",fact_res)
import time

max_tries = 5
number_of_attempts = 0
wait_time = 1

while number_of_attempts < max_tries:
    number_of_attempts += 1
    print("Attempt =",number_of_attempts,"wait =",wait_time,"s")
    time.sleep(wait_time)
    wait_time *= 2
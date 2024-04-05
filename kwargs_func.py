def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("Key is =",key,"and Value =",value)

print_kwargs(name="shaktiman", power="lazer")
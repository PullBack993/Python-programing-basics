def create_adder(x):
    def adder(y):
        return x + y

    return adder


add_15 = create_adder(15)

print("The result is", add_15(10))


# Returning different function
def outer(x):
    return x * 10


def my_func():
    # returning different function
    return outer


# storing the function in res
res = my_func()

print("\nThe result is:", res(10))
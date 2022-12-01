import itertools


def pow_gen(base: int):
    for i in itertools.count(0, 1):
        res = (base ** i)
        yield res    # TODO записать функцию-генератор


if __name__ == "__main__":
    pow_numbers = pow_gen(10)

    for _ in range(5):
        print(next(pow_numbers))

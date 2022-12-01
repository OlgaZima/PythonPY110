def min_len_check(fn):
    def wrapper(arg):
        if not len(arg) >= 10:
            raise ValueError('Строка слишком короткая')
        res = fn(arg)
        return res
    return wrapper


@min_len_check
def some_func(str_arg: str):
    ...


if __name__ == "__main__":
    some_func("Hello, World!!!")  # всё хорошо

    some_func("Short str")  # ValueError("Строка слишком короткая")

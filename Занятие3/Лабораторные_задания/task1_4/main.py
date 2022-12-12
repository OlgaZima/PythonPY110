INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open(INPUT_FILE, 'r') as f_input, open(OUTPUT_FILE, 'w') as f_output:
        for line_ in map(str.upper, f_input):
            f_output.write(line_)
    ...  # TODO перезаписать содержимое одного файла в другой


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")

def pattern_a():
    for row in range(1, 7):
        for col in range(1, row + 1):
            print(col, end="")
        print()


def pattern_b():
    for row in range(6, 0, -1):
        for col in range(1, row + 1):
            print(col, end="")
        print()


def pattern_c():
    for i in range(1, 7):
        print(" " * (7 - 1 - i), end="")
        for j in range(i, 0, -1):
            print(j, end="")
        print()


def pattern_d():
    for i in range(6, 0, -1):
        print(" " * (7 - 1 - i), end="")
        for j in range(1, i + 1):
            print(j, end="")
        print()


if __name__ == "__main__":
    print("---Pattern A---")
    pattern_a()
    print("---Pattern B---")
    pattern_b()
    print("---Pattern C---")
    pattern_c()
    print("---Pattern D---")
    pattern_d()

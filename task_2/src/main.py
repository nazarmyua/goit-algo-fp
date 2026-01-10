from pythagorean_tree import PythagoreanTree


def get_recursion_depth():
    while True:
        try:
            depth = int(input("Введіть рівень рекурсії (1-15): "))
            if 1 <= depth <= 15:
                return depth
            else:
                print("Помилка: рівень рекурсії має бути від 1 до 15")
        except ValueError:
            print("Помилка: введіть ціле число")


def main():
    depth = get_recursion_depth()
    print()

    tree = PythagoreanTree()
    tree.visualize(depth)


if __name__ == "__main__":
    main()

def print_arbol(size=10):
    print(' ' * (size - 2) + '*')

    for i in range(size - 1):
        zero = '0' * (2 * i + 1)
        espacios = ' ' * (size - i - 2)
        print(espacios + zero)

if __name__ == '__main__':
    print_arbol()

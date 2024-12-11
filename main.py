import time
import math
import matplotlib.pyplot as plt


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def build_tree(values):
    nodes = []
    for value in values:
        if value == "x":
            nodes.append(None)  # Az 'x' értékű csomópontokat None-ként kezeljük
        elif value == ".":
            nodes.append(None)
        else:
            nodes.append(Node(int(value)))

    # Gyerekcsúcsok hozzárendelése
    for i in range(len(nodes)):
        if nodes[i] is not None:
            for j in range(1, 4):
                child_index = i * 3 + j
                if child_index < len(nodes) and nodes[child_index] is not None:
                    nodes[i].children.append(nodes[child_index])

    return nodes[0]  # A gyökér visszaadása


def minErtek(node):
    """MIN lépés."""
    if not node.children:
        return int(node.value) # a hasznossaga

    minErtek = math.inf
    for child in node.children:
        minErtek = min(minErtek, maxErtek(child))
    return minErtek


def maxErtek(node):
    """MAX lépés."""
    if node is None:
        return 3  # a hasznossaga
    if not node.children:
        return int(node.value)  # a hasznossaga

    maxErtek = -math.inf
    for child in node.children:
        maxErtek = max(maxErtek, minErtek(child))
    return maxErtek


def min_max_algorithm(root):
    """MIN-MAX algoritmus futtatása a gyökér csúcstól kiindulva."""
    return maxErtek(root)


def time_plot(data):
    """Futási idő plotolása különböző bemenetekre."""
    roots = []
    times = []

    # Építsünk több fát a bemenetből, különböző részletekkel
    for i in range(1, len(data) + 1):
        partial_data = data[:i]
        root = build_tree(partial_data)
        roots.append(root)

    # Mérjük a futási időket minden fára
    for root in roots:
        start_time = time.time()
        max_profit = maxErtek(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

    # Plot készítése
    plt.plot(range(1, len(times) + 1), times, marker='o', linestyle='-')
    plt.title('Futási idő különböző méretű fákra')
    plt.xlabel('Bemeneti adatok száma')
    plt.ylabel('Futási idő (másodperc)')
    plt.grid(True)
    plt.show()

def print_tree(node, depth=0):
    """Rekurzívan kiírja a fát szintek szerint."""
    if node is None:
        return
    print("  " * depth + str(node.value))
    for child in node.children:
        print_tree(child, depth + 1)

def main():
    """A főprogram, amely fogadja a bemenetet és kiírja az eredményt."""
    input_string = input("Kérem adja meg a fát listaként ábrázolva: ")
    data = input_string.split()

    # Fa felépítése a bemenet alapján
    root = build_tree(data)

    print('\nA teljes fa kiírva szintek szerint:')
    print_tree(root)
    print()
    # MIN-MAX algoritmus futtatása és időmérés
    start_time = time.time()
    result = min_max_algorithm(root)
    end_time = time.time()

    print(f"A maximálisan elérhető nyereség: {result}")
    print(f"Futási idő: {end_time - start_time:.18f} sec") # a 9f szinte mindig csak 0-kból állt, a 18f informatívabb

    time_plot(data)


if __name__ == "__main__":
    main()

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
        if value == "x" or value == ".":
            nodes.append(None)
        else:
            nodes.append(Node(int(value)))

    # Gyerekcsúcsok hozzárendelése
    for i in range(len(nodes)):
        if nodes[i] is not None:
            for j in range(1, 4):
                child_index = i * 3 + j
                if child_index < len(nodes):
                    nodes[i].children.append(nodes[child_index])

    return nodes[0] if nodes else None


def min_value(node):
    """MIN lépés."""
    if node is None:
        return math.inf
    if not node.children or all(child is None for child in node.children):
        return node.value

    min_val = math.inf
    for child in node.children:
        if child is not None:
            min_val = min(min_val, max_value(child))
    return min_val


def max_value(node):
    """MAX lépés."""
    if node is None:
        return -math.inf
    if not node.children or all(child is None for child in node.children):
        return node.value

    max_val = -math.inf
    for child in node.children:
        if child is not None:
            max_val = max(max_val, min_value(child))
    return max_val


def min_max_algorithm(root):
    """MIN-MAX algoritmus futtatása a gyökér csúcstól kiindulva."""
    return max_value(root)


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
        max_profit = max_value(root)
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
    input_string = input("Kérem adja meg a fát listaként ábrázolva: ")
    data = input_string.split()

    root = build_tree(data)
    print_tree(root)

    start_time = time.time()
    result = min_max_algorithm(root)
    end_time = time.time()

    print(f"A maximálisan elérhető nyereség: {result}")
    print(f"Futási idő: {end_time - start_time:.9f} sec")

    time_plot(data)


if __name__ == "__main__":
    main()

import time
import math


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


def min_value(node):
    """MIN lépés."""
    if not node.children:
        return int(node.value)

    min_val = math.inf
    for child in node.children:
        min_val = min(min_val, max_value(child))
    return min_val


def max_value(node):
    """MAX lépés."""
    if node is None:
        return 3
    if not node.children:
        return int(node.value)

    max_val = -math.inf
    for child in node.children:
        max_val = max(max_val, min_value(child))
    return max_val


def min_max_algorithm(root):
    """MIN-MAX algoritmus futtatása a gyökér csúcstól kiindulva."""
    return max_value(root)


def main():
    """A főprogram, amely fogadja a bemenetet és kiírja az eredményt."""
    input_string = input("Kérem adja meg a fát listaként ábrázolva: ")
    data = input_string.split()

    # Fa felépítése a bemenet alapján
    root = build_tree(data)

    # MIN-MAX algoritmus futtatása és időmérés
    start_time = time.time()
    result = min_max_algorithm(root)
    end_time = time.time()

    print(f"A maximálisan elérhető nyereség: {result}")
    print(f"Futási idő: {end_time - start_time:.9f} sec")


if __name__ == "__main__":
    main()

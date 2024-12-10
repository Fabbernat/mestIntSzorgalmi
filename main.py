import time


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def build_tree(values):
    nodes = []
    for value in values:
        if value == "x":
            nodes.append(Node(value))
        elif value == ".":
            nodes.append(None)
        else:
            nodes.append(Node(int(value)))

    # Gyerekcsúcsok hozzárendelése
    for i in range(len(nodes)):
        if nodes[i] is not None:
            for j in range(1, 4):
                child_index = i * 3 + j
                if child_index < len(nodes):
                    if nodes[child_index] is not None:
                        nodes[i].children.append(nodes[child_index])

    return nodes[0]  # A gyökér visszaadása


def min_max(node):
    """
    A Min-Max algoritmus implementációja.
    """
    if not node.children:
        return node.value
    elif node.value == 'x':  # MAX csúcs
        return max(min_max(child) for child in node.children)
    else:  # MIN csúcs
        return min(min_max(child) for child in node.children)

def alfa_beta(node, alfa, beta):
    """
    Az Alfa-Beta vágás algoritmus implementációja.
    """
    if not node.children:
        return node.value
    elif node.value == 'x':  # MAX csúcs
        max_ertek = float('-inf')
        for child in node.children:
            max_ertek = max(max_ertek, alfa_beta(child, alfa, beta))
            if max_ertek >= beta:
                return max_ertek
            alfa = max(alfa, max_ertek)
        return max_ertek
    else:  # MIN csúcs
        min_ertek = float('inf')
        for child in node.children:
            min_ertek = min(min_ertek, alfa_beta(child, alfa, beta))
            if alfa >= min_ertek:
                return min_ertek
            beta = min(beta, min_ertek)
        return min_ertek

def main():
    """
    A program fő függvénye.
    """
    tree_str = input("Kérem adja meg a fát listaként ábrázolva: ")
    tree_list = tree_str.split()

    # A fa felépítése
    tree = build_tree(tree_list)

    # Min-Max algoritmus futtatása és idő mérése
    start_time = time.time()
    max_nyereség_minmax = min_max(tree)
    end_time = time.time()
    futasi_ido_minmax = end_time - start_time

    # Alfa-Beta vágás futtatása és idő mérése
    start_time = time.time()
    max_nyereség_alfabeta = alfa_beta(tree, float('-inf'), float('inf'))
    end_time = time.time()
    futasi_ido_alfabeta = end_time - start_time

    # Eredmények kiírása
    print("\nMin-Max algoritmus:")
    print(f"A maximálisan elérhető nyereség: {max_nyereség_minmax}")
    print(f"Futási idő: {futasi_ido_minmax:.6f} sec")

    print("\nAlfa-Beta vágás:")
    print(f"A maximálisan elérhető nyereség: {max_nyereség_alfabeta}")
    print(f"Futási idő: {futasi_ido_alfabeta:.6f} sec")

if __name__ == "__main__":
    main()
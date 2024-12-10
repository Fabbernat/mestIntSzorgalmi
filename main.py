# author: Fabbernat URX5VP

import time
import matplotlib.pyplot as plt

INF = float('inf')
n_szomszedai = []


def vegallapot(n: int) -> bool:
    # Le kell ellenorizni, hogy a parameterben kapott objectnek van-e > operatora, mert ha nincs akkor Runtime Errort kapunk
    if hasattr(n, '__gt__') and callable(getattr(n, '__gt__')):
        return n > 0
    else:
        return False


def hasznossag(n: int | float) -> int | float:
    return n ** 2


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def build_tree(values):
    nodes = [Node(value) if value is not None else None for value in values if values is not None]
    for i in range(len(values)):
        if nodes[i] is not None:  # Csak nem üres csucsokhoz adunk gyereket
            for j in range(1, 4):  # Három gyerek
                child_index = i * 3 + j
                if child_index < len(values) and nodes[child_index] is not None:
                    nodes[i].add_child(nodes[child_index])
    return nodes[0]  # A gyökér csucsot adjuk vissza

# Max érték keresése
def max_value(node):
    if node is None:
        return -INF
    if not node.children:  # Levélcsúcs
        return node.value

    valid_children_values = [max_value(child) for child in node.children if child is not None and isinstance(child.value, (int, float))]
    return max(valid_children_values) if valid_children_values else None
    # Ha minden gyermek None, akkor None a visszatérési érték


# Futási idő mérése és plottolása
def time_plot(tree):
    # Példa fák


    times = []

    for tree_values in tree:
        # Építsük meg a fát
        root = build_tree(tree_values)

        # Mérjük a futási időt
        start_time = time.time()
        max_profit = max_value(root)
        elapsed_time = time.time() - start_time
        times.append(elapsed_time)

        print(f"Fa: {tree_values}")
        print(f"Maximális nyereség: {max_profit}, Futási idő: {elapsed_time:.9f} sec")

    # Futási idő grafikon
    plt.plot(range(1, len(times) + 1), times, marker='o')
    plt.title('Futási idő grafikon')
    plt.xlabel('Fa indexe')
    plt.ylabel('Futási idő (sec)')
    plt.show()

def try_parse(value):
    try:
        return int(value)
    except ValueError:
        return None

def main():
    # Tetszoleges inputtal, parancssorbol indithato
    input_tree_string = input("Kérem adja meg a fát listaként ábrázolva:\n")
    input_list = input_tree_string.split()
    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip()

    # Átalakítjuk az értékeket
    # Ha nem tudja átparseolni int-té, akkor csak simán None-t adunk vissza
    values = [try_parse(x) if x not in ("x", ".", " ") else 'x' for x in input_list]

    # A kapott sztringbol felepıtjuk a fat a memoriaba
    built_tree = build_tree(values)
    max_val = max_value(built_tree)


    # Futási idő mérés és grafikon
    time_plot(values)

if __name__ == "__main__":
    main()

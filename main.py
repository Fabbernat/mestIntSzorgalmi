import time
import matplotlib.pyplot as plt

INF = float('inf')
n_szomszedai = []


def vegallapot(n: int) -> bool:
    # Check if the object has a valid > operator
    if hasattr(n, '__gt__') and callable(getattr(n, '__gt__')):
        return n > 0
    else:
        return False


def hasznossag(n: int | float) -> int | float:
    return n ** 2


def build_tree(values):
    nodes = [Node(value) if value != "x" else None for value in values]
    for i in range(len(values)):
        if nodes[i] is not None:  # Csak nem üres csomópontokhoz adunk gyereket
            for j in range(1, 4):  # Három gyerek
                child_index = i * 3 + j
                if child_index < len(values) and nodes[child_index] is not None:
                    nodes[i].add_child(nodes[child_index])
    return nodes[0]  # A gyökér csomópontot adjuk vissza


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)


def alpha_beta(root, param, inf, param1):
    pass


# Min érték keresése
def min_value(node):
    if not node.children:  # Levélcsúcs
        return node.value

    # Handle None values in children
    valid_children_values = [max_value(child) for child in node.children if
                             child is not None and max_value(child) is not None]
    if not valid_children_values:  # If all children are None or have None values, return None
        return None
    return min(valid_children_values)


# Max érték keresése
def max_value(node):
    if not node.children:  # Levélcsúcs
        return node.value

    # Handle None values in children
    valid_children_values = [min_value(child) for child in node.children if
                             child is not None and min_value(child) is not None]
    if not valid_children_values:  # If all children are None or have None values, return None
        return None
    return max(valid_children_values)


# Futási idő mérése és plottolása
def time_plot():
    times = []
    return times


def main():
    tree_string = input("Kérem adja meg a fát listaként ábrázolva:\n")
    input_list = tree_string.split()
    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip()

    # Átalakítjuk az értékeket
    values = [int(x) if x != "x" and x != "." else None for x in input_list]

    # Fát építünk
    root = build_tree(values)

    # Futási idő mérésére szolgáló változók
    times = []

    # Elindítjuk a keresést és mérjük a futási időt
    start_time = time.time()
    max_profit = max_value(root)
    elapsed_time = time.time() - start_time
    times.append(elapsed_time)

    # Eredmény és futási idő kiírása
    print(f"A maximálisan elérhető nyereség: {max_profit}")
    print(f"Futási idő: {elapsed_time:.9f} sec")

    # Futási idő grafikon
    plt.plot(times)
    plt.title('Futási idő grafikon')
    plt.xlabel('Döntések száma')
    plt.ylabel('Futási idő (sec)')
    plt.show()


if __name__ == "__main__":
    main()

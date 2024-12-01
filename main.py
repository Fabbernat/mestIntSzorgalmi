import time
# import matplotlib.pyplot as plt

INF = float('inf')
n_szomszedai = []  # Szomszédok tárolása


# A végállapotot meghatározó függvény
def vegallapot(n: int) -> bool:
    return n > 0


# Hasznosság függvény
def hasznossag(n):
    return n ** 2  # Példa hasznosság függvény


# Csomópontok létrehozása
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        if child:  # Csak nemüres csomópontokat adunk hozzá
            self.children.append(child)


# Fák felépítése
def build_tree(values):
    nodes = [Node(value) if value is not None else None for value in values]
    for i in range(len(values)):
        if nodes[i] is not None:  # Csak nem üres csomópontokhoz adunk gyereket
            for j in range(1, 4):  # Három gyerek
                child_index = i * 3 + j
                if child_index < len(values) and nodes[child_index] is not None:
                    nodes[i].add_child(nodes[child_index])
    return nodes[0]  # A gyökér csomópontot adjuk vissza


# Min érték keresése
def min_value(node):
    if not node.children:  # Leaf node
        return node.value

    return min(max_value(child) for child in node.children)


# Max érték keresése
def max_value(node):
    if not node.children:  # Leaf node
        return node.value

    return max(min_value(child) for child in node.children)


# A MAX és MIN értékek keresésének idejét mérjük
def time_plot():
    times = []

    def record_time(start_time):
        times.append(time.time() - start_time)

    return times, record_time


def main():
    # Kérje be az inputot
    tree_string = input("Kérem adja meg a fát listaként ábrázolva:\n")
    input_list = tree_string.split()

    # Átalakítjuk az értékeket
    values = [int(x) if x != "x" and x != "." else None for x in input_list]

    # Fát építünk
    root = build_tree(values)

    # Futási idő mérésére szolgáló változók
    times, record_time = time_plot()

    # Elindítjuk a keresést és mérjük a futási időt
    start_time = time.time()
    max_profit = max_value(root)
    record_time(start_time)

    elapsed_time = time.time() - start_time

    # Eredmény és futási idő kiírása
    print(f"A maximálisan elérhető nyereség: {max_profit}")
    print(f"Futási idő: {elapsed_time:.9f} sec")

    # Futási idő grafikon
    # plt.plot(times)
    # plt.title('Futási idő grafikon')
    # plt.xlabel('Döntések száma')
    # plt.ylabel(f'Futási idő: {elapsed_time} sec')
    # plt.show()


if __name__ == "__main__":
    main()

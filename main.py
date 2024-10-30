import math
import time
from AlfaBeta import MaxErtek, MinErtek
INF = float('inf')
n_szomszedai = []


def vegallapot(n: int) -> bool:
    return n > 0


def hasznossag(n):
    return n ** 2



def build_tree(tree_string):
    return Node(tree_string)


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []


def alpha_beta(root, param, inf, param1):
    pass


def main():
    tree_string = input("”Kérem adja meg a fát listaként ábrázolva:")
    root = build_tree(tree_string)
    """
    Ez a string egy fa t¨ombben val´o FIX m´odon megadott reprezent´aci´oja
    (l´asd: 2.1 fejezet). A kapott stringb˝ol ´ep´ıtse fel a f´at a mem´ori´aba. Egy cs´ucs ´abr´azol´as´ahoz
    haszn´aljunk oszt´alyt. Az elt´arolt f´an hajtsa v´egre a MINMAX vagy ALFABETA algoritmusok egyik´et. ´
    A v´egrehajt´as ut´an k´et dolog jelenjen meg outputk´ent. Egyr´eszt ´ırja ki a konzolra az algoritmus fut´asi
    idej´et. Valamint ´ırja ki a gy¨ok´er cs´ucsban el´erhet˝o maxim´alis nyeres´eget.
    """
    start_time = time.time()
    result = alpha_beta(root, -math.inf, math.inf, True)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Futási idő: {duration} sec")

if __name__ == "__main__":
    main()

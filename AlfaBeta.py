from main import vegallapot, hasznossag, INF, n_szomszedai

def MaxErtek(n, alfa, beta):
    if vegallapot(n):
        return hasznossag(n)

    max = -INF
    for a in n_szomszedai:
        max = max(max, MinErtek(a, alfa, beta))
        if max >= beta:
            return max

        alfa = max(max, alfa)
    return max


def MinErtek(n, alfa, beta):
    if vegallapot(n):
        return hasznossag(n)

    min = +INF
    for a in n_szomszedai:
        min = min(min, MaxErtek(a, alfa, beta))
        if alfa >= min:
            return min
        beta = min(min, beta)
    return min

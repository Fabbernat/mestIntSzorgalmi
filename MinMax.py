from main import vegallapot, hasznossag, INF, n_szomszedai, maxErtek


def minmax(n):
    def max_value(n):
        if vegallapot(n):
            return hasznossag(n)

        max = -INF
        for a in n_szomszedai:
            max = max(max, min_value(a))
        return max

    def min_value(n):
        if vegallapot(n):
            return hasznossag(n)

        min = +INF
        for a in n_szomszedai:
            min = min(min, max_value(a))

        return min

    return min_value(n), max_value(n)

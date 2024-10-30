from main import vegallapot, hasznossag, INF, n_szomszedai

def MaxErtek(n):
     if vegallapot(n):
          return hasznossag(n)

     max = -INF
     for a in n_szomszedai:
          max = max(max, MinErtek(a))
     return max


def MinErtek(n):
     if vegallapot(n):
          return hasznossag(n)

     min = +INF
     for a in n_szomszedai:
          min = min(min, MaxErtek(a))

     return min
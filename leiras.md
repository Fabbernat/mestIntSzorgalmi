# Mesterséges intelligencia, szorgalmi feladat

## 1 Követelmények
A félév során le lehet implementálni bármely programozási nyelven a **MIN-MAX** vagy **ALFA-BETA**
algoritmusok egyikét. A program nem kell GUI-val rendelkezzen. Minimum követelmény, hogy
tetszőleges inputtal, parancssorból indítható legyen. Az algoritmus helyes implementálásával 4 pont
szerezhető. Ez a plusz pont a kettes érdemjegybe nem számít bele, viszont feljebb igen. A kiszh-k és
a szorgalmi pontjaival összesen egy jegyet lehet javítani.
Az algoritmusok bővebb leírása a gyakorlati és az előadás jegyzetekben is megtalálható, valamint
neten is sok anyag áll rendelkezésre. Az algoritmusok pszeudokódja a dokumentum végén látható.
Implementálás során ennek a pszeudokódnak vissza kell köszönnie.
# 2 A program működése
Közvetlenül indítás után írja ki konzolra, hogy "Kérem adja meg a fát listaként ábrázolva:", ezután
pedig várjon is egy input stringet. Ez a string egy fa tömbben való FIX módon megadott reprezentációja
(lásd: 2.1 fejezet). A kapott stringből építse fel a fát a memóriába. Egy csúcs ábrázolásához
használjunk osztályt. Az eltárolt fán hajtsa végre a MINMAX vagy ALFABETA algoritmusok egyikét.
A végrehajtás után két dolog jelenjen meg outputként. Egyrészt írja ki a konzolra az algoritmus futási
idejét. Valamint írja ki a gyökér csúcsban elérhető maximális nyereséget.
## 2.1 Input példa
A fenti fa az alábbi módon tárolható tömbben (ahol a ’.’ üres helyet jelöl):
3 3 2 1 3 12 8 2 4 6 14 1 5 . . . 12 -7 . . . . 2 . . 4 . . . . . . . . 1 . . . . .
Minden elemre igaz, hogy az elem fiait az alábbi képlettel lehet elérni:
• első fiú: i ∗ 3 + 1, ahol i változó a tömbbéli index
• második fiú: i ∗ 3 + 2, ahol i változó a tömbbéli index
• harmadik fiú: i ∗ 3 + 3, ahol i változó a tömbbéli index

A fenti példában a gyökér csúcs, a tömbb nuladik eleme. Az ő gyerekei a tömbb 0*3+1 = 1.,
0*3+2=2. és 0*3+3. elemei.
A programba való beadáskor csak a levélcsúcsok nyereményértéke ismert, innen kell az algoritmusnak kiszámolni, hogy mi lesz a gyökércsúcsban a nyeremény. Emiatt minden belső csúcsot ”x”-el
jelölünk az inputban. Ettől még a korábbi szabály él, tehát ugyan ennek a fának a string reprezentáció
inputként a programban:
x x x x 3 x 8 x x 6 14 x 5 . . . 12 -7 . . . . 2 . . 4 . . . . . . . . 1 . . . . .
## 2.2 Output példa
A maximálisan elérhető nyereség: 3 (Az input példánál). Futási idő: 1.233435324 sec
# 3 Beadás
A kész kódot zipként csomagolt formátumba kell elküldeni a vetrabm@inf.u-szeged.hu email címre. A
külső mappában legyen egy README.md fájl, amely tartalmazza a kód fordításának és használatának
pontos lépéseit. Beadási határidő a szorgalmi időszak vége (december 16. éjfél)
# 4 Pszeudokódok
## 4.1 MIN-MAX
```python
def MaxErtek(n):
     if vegallapot(n):
          return hasznossag(n)

     max = -INF
     for a in n_szomszedai:
          max = max(max, MinErtek(a))
     return max
```

Tehát a MAX játékos döntésekor azt a leszármazott csúcsot fogom keresni, ahol a MIN játékos a
legtöbb pontot érné el. Miért? Mert a MIN játékos minimalizálásra törekszik, tehát arra akarom
rákényszeríteni, hogy minél kisebb hasznosságú csúcsot tudjon csak végrehajtani.
```python
def MaxErtek(n):
     if vegallapot(n):
          return hasznossag(n)

     max = -INF
     for a in n_szomszedai:
          max = max(max, MinErtek(a))
     return max
```

Tehát a MIN játékos döntésekor azt a leszármazott csúcsot fogom keresni, ahol a MAX játékos a
legkevesebb pontot érné el. Miért? Mert a MAX játékosnak az a jó, ha minél nagyobb értékű állapotba
jusson (maximalizálásra törekszik), tehát arra akarom rákényszeríteni, hogy minél kisebb hasznosságú
csúcsot tudjon csak választani.

# 4.2 ALFA-BETA 
```python

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
```
```python
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
```
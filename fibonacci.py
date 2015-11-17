def fibonacci():
    i = 1
    temp = 0
    # Die erste Fibonaccizahl ist als 1 festgelegt
    yield i

    while (i > 0):
        # für die nächste Fibonacci-Zahl werden BEIDE Vorgänger benötigt
        list = [temp, i]
        yield list[0] + list[1]
        temp = list[1]
        i = list[0] + list[1]

# Testen
gen = fibonacci()
for i in gen:
    print(i)
    if i > 10000:
        break

def qsort(L):
    if L:
        return qsort([x for x in L[1:] if x < L[0]]) \
        + L[:1] + qsort([x for x in L[1:] if x >= L[0]])
    return []

list = [0, 33, 22, 11, 55, 44]
print(qsort(list))

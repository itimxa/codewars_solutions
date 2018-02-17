""" Core idea of this Kata is to realize next operation
           X[i] > X[j] then X[i] = X[i] - X[j]
script will stop when all items in input list become equal
and return the sum of equal elements """

def solution(a):
    while a.count(a[0]) != len(a):
        minimal = min(a)
        for i in range(len(a)):
            if a[i] != minimal and a[i] % minimal != 0:
                a[i] = a[i] % minimal
            else:
                a[i] = minimal
    return sum(a)

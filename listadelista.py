
def lis(l):
    if not isinstance(l, list):
        return l
    elif isinstance(l, list):
        for j in l:
            return j


if __name__ == '__main__':
    list0 = [1, 2, [3, 4], 5, [[6, 7], [8, 9]]]
    for l in list0:
        print(lis(l))

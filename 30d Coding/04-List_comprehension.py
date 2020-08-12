if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    xList = list(range(x+1))
    yList = list(range(y+1))
    zList = list(range(z+1))

    results = [[x, y, z] for x in xList for y in yList for z in zList if (x + y + z) != n]

    print(results)
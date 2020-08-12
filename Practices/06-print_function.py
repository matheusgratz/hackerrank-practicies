if __name__ == '__main__':
    n = int(input())
    numL=[]
    for num in range(n):
        numL.append(num+1)
    print(*numL, sep='')
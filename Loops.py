def squr(n):
    r = n
    r = n*n
    print(r)

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        squr(i)
        i = i+1
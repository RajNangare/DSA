def bubble_sort(a):
    n=len(a)
    for i in range(n):
        for j in range(n-1):
           if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
    return a
if __name__ =="__main__":
    g=list(map(int,input().split()))
    bubble_sort(g)
    print(g)
def linear_search(a,n):
    for i in range(len(a)):
        if a[i]==n:
            return i
if __name__=="__main__":
    list=list(map(int,input().split()))
    n=int(input())
    list.sort()
    print(list)
    print(linear_search(list,n))
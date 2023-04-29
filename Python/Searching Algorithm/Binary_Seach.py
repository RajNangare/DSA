def rec_binarysearch(a,n):
    k=len(a)//2
    if a[k//2]==n:
        return k//2
    elif a[k//2]<n:
        rec_binarysearch(a[k//2:n])
    pass
    
def some(a,i,k,n):  
    print a[i]
    i=i-1
    k=k+1
    if n==k :
    	return 0 
    else:
    	some(a,i,k,n)
a =[1,2,3,4]
n=4
i=-1
k=0
some(a,i,k,n)





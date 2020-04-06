# function to print triplets with 0 sum  
def findTriplets(arr, n): 
    for i in range(0,n-1):
        s=set()
        for j in range(i+1,n):
            x=-(arr[i]+arr[j])
            if x in s:
                print(x,arr[i],arr[j])
            else:
               s.add(arr[j])
    


a=[-1, 0, 1, 2, -1, -4]
length=len(a)
findTriplets(a,length)













































found = False
    for i in range(n - 1): 
  
        # Find all pairs with sum  
        # equals to "-arr[i]"  
        s = set() 
        for j in range(i + 1, n): 
            x = -(arr[i] + arr[j]) 
            if x in s: 
                print(x, arr[i], arr[j]) 
                found = True
            else: 
                s.add(arr[j]) 
    if found == False: 
        print("No Triplet Found")
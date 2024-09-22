#merge sort 

def merge(arr, low, mid, high):
    c=[]
    #lowest value 
    start1 = low 
    #middle value 
    start2 = mid+1
#if the (start1) lowest valuse is lower than the middle, and start2 highest value is lower then the highest value
    #then compare the elemnts and re arrnge them and put them into the list 
    while start1<=mid and start2<=high:
        if arr[start1] <arr[start2]:
            c.append(arr[start1])
            start1+=1
        else: 
            c.append(arr[start2])
            #moving the index by 1 
            start2+=1 
    #just comparing the lowest and middle element and putting it in place 
    while start1<= mid :
        c.append(arr[start1]) #value append 
        start1+=1
#comparing highest element
    while start2<= high:
        c.append(arr[start2])
        start2+=1 

    k = 0 
    for i in range(low, high+1):
        #i = zeroth element
        #i = k = 0, 0th element from c[0] is added to arr[0] element and similarly added to the rest also from the list 
        #merging happening 
        arr[i] = c[k]
        k+=1

def mergesort(arr,low,high):
    if low<high:
        mid = (low + high)//2 #// is floor division where we ignore the decialm position because the index num cant be a deciaml 
        mergesort(arr, low,mid) # first seperation of sublist 
        mergesort(arr, mid+1, high) #second seperation 
        merge(arr,low,mid,high)#combining and sorting the list recursively 


list2 = [13,16,12,1,8,4,6,10]
n = len(list2)
high = n-1 #index number of lat value
mergesort(list2, 0, high)
print(list2)






    





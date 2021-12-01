def insertionSort(arr,start,end):
    arr=list(arr)
    def swap(i): #swap fucntion 
        arr[i-1]=arr[i]+arr[i-1]
        arr[i]=arr[i-1]-arr[i]
        arr[i-1]=arr[i-1]-arr[i]

    for i in range(start+1,end): #primary loop
        j=i #subindex
        while arr[j]<arr[j-1] and j>start: 
            # untill less than previous element 
            # and greater than starting index
            swap(j)
            j=j-1
    return arr


arr=[1,5,5,6,2,6,86,5,3,9,9,9,6]

print(insertionSort(arr, 0, len(arr)))
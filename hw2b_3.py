#heapsort algorithm 
#take an array and sort it in ascending order using the heapsort algorithm

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def heapify(arr, parent, upper):
    while (True):
        #parent represents the current parent index so l and r represent the starting indexes of the childern to that parent.
        l, r = parent*2+1, parent*2+2
        #upper is the upper bound of the array currently so if l and r are less than the upper bound that means they are valid indexes.
        #this also means that two children exist
        if max(l, r) < upper:
            #if the parent is greater than the children then we are done
            if arr[parent] >= max(arr[l], arr[r]): break
            #check which node is bigger and swap it with the parent then set the swaped value to be the new parent
            elif arr[l] > arr[r]:
                swap(arr, parent, l)
                parent = l
            else:
                swap(arr, parent, r)
                parent = r
        #left child node exists 
        elif l < upper:
            if arr[l] > arr[parent]:
                swap(arr, parent, l)
                parent = l
            #if the child isn't bigger than the parent we are done
            else: break
        elif r < upper:
            if arr[r] > arr[parent]:
                swap(arr, parent, r)
                parent = r
            else:break
        #if there are no children we have nothing to do
        else: break

def heapsort(arr):
    #HEAPIFY INTO MAX HEAP
    #(len(arr)-2) // 2 ; is the last parent node in a array. We don't care about any nodes after since they won't have any children to swap with
    #we want to go through the array until the first element at 0 (python range function is not inclusive so we need to go until -1 to reach 0)
    for i in range((len(arr)-2) // 2, -1, -1):
        heapify(arr, i, len(arr))
    #SORT ARRAY
    #we don't need to worry about iterating to the first element because by the time we get to there it is already sorted since it is the last element
    for upper in range(len(arr)-1, 0, -1):
        #the very first element in a max heap is always going to be the largest element in the heap
        #we must swap the first element and the last element that isn't sorted yet 
        #upper is the upper bound of the array that isn't sorted yet
        swap(arr, 0, upper)
        heapify(arr, 0, upper)

arr = [22, 11, 88, 66, 55, 77, 33, 44]
heapsort(arr)
print(arr)  
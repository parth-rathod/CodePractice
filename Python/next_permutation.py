import random
def next_permutation(arr):
    print("The given arr is :", arr)
    inv_index = len(arr) - 2
    while inv_index >= 0 and (arr[inv_index] >= arr[inv_index+1]):
        inv_index -= 1
    
    #There is no next element
    if inv_index == -1:
        return []
    
    for i in reversed(range(inv_index+1,len(arr))):
        if arr[i] > arr[inv_index]:
            arr[i],arr[inv_index] = arr[inv_index],arr[i]
            break
    
    arr[inv_index+1:] = reversed(arr[inv_index+1:])
    return arr



def previous_permutation(arr):
    print("The given arr is :", arr)
    inv_index = len(arr) - 2
    while inv_index >= 0 and (arr[inv_index] <= arr[inv_index+1]):
        inv_index -= 1
    
    #There is no next element
    if inv_index == -1:
        return []
    
    for i in reversed(range(inv_index+1,len(arr))):
        if arr[i] < arr[inv_index]:
            arr[i],arr[inv_index] = arr[inv_index],arr[i]
            break
    
    arr[inv_index+1:] = reversed(arr[inv_index+1:])
    return arr

if __name__ == "__main__":
    next_ans = next_permutation([random.choice([1,2,3,4]) for _ in range(4)])
    print("Next Permutaion is:",next_ans)

    arr = [1,3,2,4,6,2]
    prev_ans = previous_permutation([random.choice([1,2,3,4]) for _ in range(4)])
    print("Previous Permutaion is:",prev_ans)
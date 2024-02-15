def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = mergeSort(left_half)
    right_half = mergeSort(right_half)

    return merge(left_half,right_half)

def merge(left,right):
    merged = []
    left_index = right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index+=1
        else:
            merged.append(right[right_index])
            right_index+=1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged

ary = [5,9,3,2,4]
print(mergeSort(ary)) 
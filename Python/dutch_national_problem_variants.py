import random

# All F before T
def all_F_before_T(arr):
    low, mid = 0, 0
    while mid <= len(arr)-1:
        if arr[mid] == "T":
            mid += 1
        else:
            arr[mid], arr[low] = arr[low], arr[mid]
            mid += 1
            low += 1
    return arr

#Categorize 4 elements
def categorize_4_elements(nums):
    low1, low2, mid, high = 0, 0, 0, len(nums)-1
    while mid <= high:
        if nums[mid] == "1":
            nums[low1], nums[mid] = nums[mid], nums[low1]
            nums[low2], nums[mid] = nums[mid], nums[low2]
            low1 += 1
            low2 += 1
            mid += 1
        elif nums[mid] == "2":
            nums[low2], nums[mid] = nums[mid], nums[low2]
            low2 += 1
            mid += 1
        elif nums[mid] == "3":
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


if __name__ == "__main__":
    ans = all_F_before_T(arr = [random.choice(["T", "F"]) for _ in range(15)])
    print(ans)
    ans = categorize_4_elements(nums= [random.choice(["1", "2", "3", "4"]) for _ in range(25)])
    print(ans)
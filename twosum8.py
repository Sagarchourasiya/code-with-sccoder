# Two sum problem of array
# Input: arr[] = {0, -1, 2, -3, 1}, target = -2 [1 + [-3] = -2]
# Output: True
def two_sum(arr, target):
    n = len(arr)
    sum = []
    for i in range(0,n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
                return [arr[i],arr[j]]
    return sum
if __name__ == "__main__":
    arr = [1,2,3,4,5]
    target = 5
    answer = two_sum(arr, target)
    print(f"TwoSum {answer}")
from typing import List


def countingSort(nums: List[int]) -> List[int]:
    l = min(nums)
    r = max(nums)
    k = r - l + 1

    count = [0] * k
    for num in nums:
        count[num - l] += 1

    output = [0] * len(nums)
    for i in range(1,k):
        count[i] = count[i-1] + count[i]

    # i = len(nums) - 1
    # while i >= 0:
    #     index = count[nums[i] - l] - 1
    #     output[index] = nums[i]
    #     count[nums[i] - l] -= 1
    #     i -= 1

    for i in range(len(nums)-1, -1, -1):
        index = count[nums[i] - l] - 1
        output[index] = nums[i]
        count[nums[i] - l] -= 1

    return output

print(countingSort([2,3,1,5,3]))
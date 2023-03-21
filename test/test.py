def single_non_duplicate(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    middle = (right + 1 - left) // 2
    while left != middle and right != middle >= 0:
        middle = (right + 1 - left) // 2
        if nums[middle] == nums[middle - 1]:
            if (right + 2 - middle) % 2 == 0:
                right = middle
            else:
                left = middle - 2

        else:
            if (right + 1 - (middle - 1)) % 2 == 0:
                right = middle - 1
            else:
                left = middle
    return nums[left]


print(singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
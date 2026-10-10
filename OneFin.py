# 1. Subarrays with Product Less Than K

# Given an array of positive integers, find all contiguous subarrays whose product is less than a given value k.
# Example:
# Input: nums = [1, 2, 4, 3], k = 9
# Output: [[1], [2], [3], [1,2], [2,4]] (valid subarrays with product < 9)


def subarray_product_less_than_k(nums, k):
    if k <= 1:
        return []

    result = []
    product = 1
    left = 0

    for right in range(len(nums)):
        product *= nums[right]           # expand window

        while product >= k:              # shrink from left
            product //= nums[left]
            left += 1

        # all subarrays ending at right,
        # starting from left..right are valid
        for i in range(left, right + 1):
            result.append(nums[i:right+1])

    return result

nums = [1, 2, 4, 3]
print(subarray_product_less_than_k(nums, 9))
# [[1],[2],[1,2],[4],[2,4],[1,2,4],[3]]


# -------------------------------------------------------------------------------------------------------------------
# 2. Fruits in Baskets Problem

# You are given an array representing different types of fruit trees arranged in a row. Each number in the array represents a type of fruit.
# You have two baskets, and each basket can hold only one type of fruit, but in unlimited quantity.
# Starting from any point and moving forward, determine the maximum number of fruits you can collect, such that you only pick fruits from at most two distinct types.

# Example:
# Input: fruits = [4, 1, 1, 2, 1, 3]
# Output: 4
# Explanation: The longest subarray with at most 2 distinct fruit types is [1, 1, 2, 1].


def total_fruit(fruits):
    basket = {}   # fruit_type → count in current window
    left = 0
    max_len = 0

    for right in range(len(fruits)):
        fruit = fruits[right]
        basket[fruit] = basket.get(fruit, 0) + 1   # add to basket

        while len(basket) > 2:                      # more than 2 types?
            left_fruit = fruits[left]
            basket[left_fruit] -= 1
            if basket[left_fruit] == 0:
                del basket[left_fruit]              # remove from basket
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len

# Test
print(total_fruit([4, 1, 1, 2, 1, 3]))  # 4
# Window [1, 1, 2, 1] — types {1, 2} — length 4
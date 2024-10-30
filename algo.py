from typing import List


def numSqr(x: int) -> int:
    if not x:
        return 0
    left, right = 1, x
    while left < right:
        mid = left + (right - left) / 2
        if x / mid >= mid:
            left = mid
        else:
            right = mid - 1
    return mid


def removeElement(nums: List[int], val: int) -> int:
    i, j = 0, len(nums) - 1
    k = 0
    while i <= j:
        if nums[i] == val:
            while nums[j] == val:
                j -= 1
            nums[i] = nums[j]
        j -= 1
        i += 1
        k += 1

    return k


if __name__ == '__main__':
    # print(numSqr(9))
    print(removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2))

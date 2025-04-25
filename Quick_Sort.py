def partition(nums):
  pivot = nums[0]

  left_half = []
  right_half = []

  for num in nums[1:]:
    if num <= pivot:
      left_half.append(num)
    else:
      right_half.append(num)

  return left_half, right_half, pivot

def QuickSort(nums):
  if len(nums) <= 1:
    return nums

  left_half, right_half, pivot = partition(nums)

  return QuickSort(left_half) + [pivot] + QuickSort(right_half)
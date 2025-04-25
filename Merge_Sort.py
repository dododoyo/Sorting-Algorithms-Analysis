def conquer(left_half, right_half):
  left_index = 0
  right_index = 0
  sorted_subarray = []

  while left_index < len(left_half) and right_index < len(right_half):
    if left_half[left_index] <= right_half[right_index]:
      sorted_subarray.append(left_half[left_index])
      left_index += 1
    else:
      sorted_subarray.append(right_half[right_index])
      right_index += 1

  while left_index < len(left_half):
    sorted_subarray.append(left_half[left_index])
    left_index += 1

  while right_index < len(right_half):
    sorted_subarray.append(right_half[right_index])
    right_index += 1

  return sorted_subarray

def divide(left, right, arr):
  if left == right:
    return [arr[left]]
  
  mid = (left + right) // 2

  left_ = divide(left, mid, arr)
  right_ = divide(mid + 1, right, arr)

  return conquer(left_, right_)

def MergeSort(arr):
  if len(arr) == 0:
    return []
  return divide(0, len(arr) - 1, arr)
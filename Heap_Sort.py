def swap(heap, i, j):
  heap[i], heap[j] = heap[j], heap[i]

def heapify_down(heap, n, current_idx):
  large_child_idx = current_idx
  left_idx = 2 * current_idx + 1
  right_idx = 2 * current_idx + 2

  if left_idx < n and heap[left_idx] > heap[large_child_idx]:
    large_child_idx = left_idx

  if right_idx < n and heap[right_idx] > heap[large_child_idx]:
    large_child_idx = right_idx

  if large_child_idx != current_idx:
    swap(heap, current_idx, large_child_idx)
    heapify_down(heap, n, large_child_idx)

def HeapSort(arr):
  n = len(arr)

  for i in range(n // 2 - 1, -1, -1):
    heapify_down(arr, n, i)

  for i in range(n - 1, 0, -1):
    swap(arr, 0, i)  
    heapify_down(arr, i, 0) 

  return arr
import matplotlib.pyplot as plt 
from random import randint
from time import time

from Heap_Sort import HeapSort
from Insertion_Sort import InsertionSort
from Quick_Sort import QuickSort
from Selection_Sort import SelectionSort
from Merge_Sort import MergeSort


def generator(n,randomness):
    if randomness not in [0, 0.5, 1]:
        raise ValueError("randomness must be 0, 0.5 or 1")
    
    if randomness == 0.5:
        return [randint(0, 100_000) for _ in range(n)]
    elif randomness == 1:
        return list(range(n))
    elif randomness == 0:
        return list(range(n, 0, -1))
    
def tester(start,stop,presortedness,steps,rep):
    solution = [[0 for _ in range(5)] for _ in range(stop // steps + 1)]
    algorithms = ['Insertion Sort', 'Merge Sort', 'Heap Sort','Quick Sort', 'Selection Sort']

    for curr_size in range(start, stop + 1, steps):
        index = curr_size // steps
        for sorter in [2,1,3,0,4]: 
            total_time = 0
            for _ in range(rep):
                arr = generator(curr_size, presortedness)
                
                start_time = time()
                if sorter == 0:
                    InsertionSort(arr)
                elif sorter == 1:
                    MergeSort(arr)
                elif sorter == 2:
                    HeapSort(arr)
                elif sorter == 3:
                    QuickSort(arr)
                elif sorter == 4:
                    SelectionSort(arr)
                end_time = time()

                total_time += (end_time - start_time)

            avg_time = total_time / rep
            solution[index][sorter] = avg_time
            print(f"Sorter {algorithms[sorter]} took {avg_time:.6f} seconds to sort {curr_size} elements")

        #save average time for all curr_size in a .txt file for each size
        # like 0.2,0.3,0.4,0.5,0.6 on a new line
        with open(f'sorting_performance_({start}-{stop})_{presortedness}_{steps}_{rep}.txt', 'a') as f:
            f.write(f"{solution[index]}\n")
        print()


    x = [i * steps for i in range(len(solution))]

    plt.figure(figsize=(12, 7))
    for i in range(5):
        plt.plot(x, [row[i] for row in solution], 
                marker='o', 
                linestyle='-', 
                linewidth=2,
                label=algorithms[i])

    plt.xlabel('Input Size', fontsize=12)
    plt.ylabel('Time Taken (seconds)', fontsize=12)
    plt.title('Sorting Algorithm Performance Comparison', fontsize=14)

    plt.legend(fontsize=10)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig(f'sorting_performance_({start}-{stop})_{presortedness}_{steps}_{rep}.png')
    plt.show()

if __name__ == "__main__":
    start = 0
    end = 100_000
    presortedness = 0.5
    steps = 5_000
    rep = 2

    tester(start,end,presortedness,steps,rep)
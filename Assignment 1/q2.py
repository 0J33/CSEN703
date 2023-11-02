import timeit
import matplotlib.pyplot as plt
import random



# q2. part a

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def find_pairs_with_sum(arr, target_sum):
    merge_sort(arr)  # Sort the array using Merge Sort

    pairs = []
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target_sum:
            pairs.append((arr[left], arr[right]))
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

    return pairs

# Example usage:
arr = [4, 7, 1, 3, 9, 2, 6]
target_sum = 10
result = find_pairs_with_sum(arr, target_sum)
print(result)



# q2. part b

# Merge Sort: The sorting part of the algorithm, 
# which sorts the input array, has a time complexity of O(n log n). 
# This is the dominating factor in the time complexity analysis.

# Binary Search: The binary search part to find pairs with the target sum is linear, 
# as we iterate through the array once. This has a time complexity of O(n).

# The overall time complexity of the algorithm is determined by the dominant factor, 
# which is the sorting step, i.e., O(n log n). 
# So, the algorithm's overall time complexity is O(n log n).



# q2. part c

# Experiment with different input sizes (n)
input_sizes = [5, 10, 100, 200, 500, 1000]
execution_times = []

for size in input_sizes:
    input_data = [random.randint(1, size) for _ in range(size)]
    target_sum = random.randint(1, size * 2)

    # Measure the execution time for the current input size
    execution_time = timeit.timeit("find_pairs_with_sum(input_data, target_sum)", globals=globals(), number=10)
    execution_times.append(execution_time)

# Plot the results
plt.plot(input_sizes, execution_times, marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (s)")
plt.title("Algorithm Scalability")
plt.show()
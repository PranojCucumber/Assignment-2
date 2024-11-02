import random
import time
import sys
import tracemalloc

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left or right)
    return result


# Generate test datasets
def generate_datasets(size):
    sorted_data = list(range(size))
    reverse_sorted_data = sorted_data[::-1]
    random_data = [random.randint(0, size) for _ in range(size)]
    return sorted_data, reverse_sorted_data, random_data

# Function to measure performance
def measure_performance(sort_func, data):
    # Measure memory usage
    tracemalloc.start()
    start_time = time.perf_counter()
    
    sorted_data = sort_func(data.copy())  # Copy data to avoid in-place sorting issues
    
    end_time = time.perf_counter()
    memory_usage = tracemalloc.get_traced_memory()[1]
    tracemalloc.stop()
    
    execution_time = end_time - start_time
    return execution_time, memory_usage

# Comparison of Quick Sort and Merge Sort
def compare_algorithms(data_size):
    sorted_data, reverse_sorted_data, random_data = generate_datasets(data_size)
    
    # Quick Sort
    print("Quick Sort Performance:")
    for data, name in zip([sorted_data, reverse_sorted_data, random_data], 
                          ["Sorted", "Reverse Sorted", "Random"]):
        execution_time, memory_usage = measure_performance(quicksort, data)
        print(f"{name} data: Time = {execution_time:.6f}s, Memory = {memory_usage / 1024:.2f} KB")
    
    # Merge Sort
    print("\nMerge Sort Performance:")
    for data, name in zip([sorted_data, reverse_sorted_data, random_data], 
                          ["Sorted", "Reverse Sorted", "Random"]):
        execution_time, memory_usage = measure_performance(merge_sort, data)
        print(f"{name} data: Time = {execution_time:.6f}s, Memory = {memory_usage / 1024:.2f} KB")

# Run comparison for a dataset size of 1000
compare_algorithms(1000)

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def swap(arr, i, j):
    if i != j:
        arr[i], arr[j] = arr[j], arr[i]

#Bubble Sort
def bubbleSort(arr):
    #zaman al
    n = len(arr)
    if n == 1:
        return
    swapped = True
    for i in range(n):
        if not swapped:
            break
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                swap(arr, j, j + 1)
                swapped = True
            yield arr
    #zaman
    #zamanların farkını alıp return et


#Selection Sort
def selectionSort(arr):
    n = len(arr)
    if n == 1:
        return
    swapped = True
    for i in range(n):
        minValue = i
        for j in range(i+1, n):
            if arr[j] < arr[minValue]:
                minValue = j
            yield arr
        swap(arr, i, minValue)
        yield arr

#Insertion Sort
def insertionSort(arr):
    n = len(arr)
    for i in range(n):
        value = arr[i]
        j = i-1
        while j >= 0 and arr[j] > value:
            arr[j+1] = arr[j]
            j = j-1
            yield arr
        arr[j+1] = value
        yield arr

#Shell Sort
def shellSort(arr):
    sublistcount = len(arr)//2
    while sublistcount > 0:
        for i in range (sublistcount, len(arr)):
            temp = arr[i]
            j = i
            while  j >= sublistcount and arr[j-sublistcount] >temp:
                arr[j] = arr[j-sublistcount]
                j -= sublistcount
            arr[j] = temp
            yield arr
        sublistcount //= 2
        yield arr

#Heap sort
def heapify(arr, i, heap_size):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2
    if left_index < heap_size and arr[left_index] > arr[largest]:
        largest = left_index
    if right_index < heap_size and arr[right_index] > arr[largest]:
        largest = right_index
    if largest != i:
        swap(arr, largest, i)
        yield from heapify(arr, largest, heap_size)
        yield arr
def heapSort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        yield from heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        yield from heapify(arr, 0, i)
        yield arr

#Radix Sort
def countingSort(arr, place):
    output = [0] * (len(arr))
    count = [0] * (10)
    for i in range(0, len(arr)):
        index = arr[i]//place
        count[index % 10] += 1
    for i in range(1,10):
        count[i] += count[i-1]
    i = len(arr)-1
    while i >= 0:
        index = arr[i]//place
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(0,len(arr)):
        arr[i] = output[i]
        yield arr
def radixSort(arr):
    max_element = max(arr)
    place = 1
    while max_element/place > 0:
        yield from countingSort(arr,place)
        place *= 10
        yield arr

#Merge Sort
def merge(arr, start, mid, end):
    merged = []
    left = start
    right = mid + 1
    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            merged.append(arr[left])
            left += 1
        else:
            merged.append(arr[right])
            right += 1
    while left <= mid:
        merged.append(arr[left])
        left += 1
    while right <= end:
        merged.append(arr[right])
        right += 1
    for i, sorted_val in enumerate(merged):
        arr[start + i] = sorted_val
        yield arr
def mergeSort(arr, start, end):
    if end <= start:
        return
    mid = start + ((end - start + 1) // 2) - 1
    yield from mergeSort(arr, start, mid)
    yield from mergeSort(arr, mid + 1, end)
    yield from merge(arr, start, mid, end)
    yield arr

#Quick Sort
def quickSort(arr, start, end):
    if start >= end:
        return
    pivot = arr[end]
    pivotIdx = start
    for i in range(start, end):
        if arr[i] < pivot:
            swap(arr, i, pivotIdx)
            pivotIdx += 1
        yield arr
    swap(arr, end, pivotIdx)
    yield arr
    yield from quickSort(arr, start, pivotIdx - 1)
    yield from quickSort(arr, pivotIdx + 1, end)

if __name__ == "__main__":
    number = int(input("Enter number of integers: "))
    method_msg = "Enter sorting method:" \
                 "\n1- Bubble Sort" \
                 "\n2- Insertion Sort" \
                 "\n3- Selection Sort " \
                 "\n4- Shell Sort " \
                 "\n5- Heap sort " \
                 "\n6- Radix sort" \
                 "\n7- Merge sort " \
                 "\n8- Quick Sort \n"
    method = input(method_msg)

    arr = [x + 1 for x in range(number)]
    random.seed(time.time())
    random.shuffle(arr)

    if method == "1":
        title = "Bubble sort"
        generator = bubbleSort(arr)
    elif method == "2":
        title = "Insertion sort"
        generator = insertionSort(arr)
    elif method == "3":
        title = "Selection sort"
        generator = selectionSort(arr)
    elif method == "4":
        title = "Shell sort"
        generator = shellSort(arr)
    elif method == "5":
        title = "Heap sort"
        generator = heapSort(arr)
    elif method == "6":
        title = "Radix sort"
        generator = radixSort(arr)
    elif method == "7":
        title = "Merge sort"
        generator = mergeSort(arr, 0, number - 1)
    else:
        title = "Quick sort"
        generator = quickSort(arr, 0, number-1)

    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")
    ax.set_xlim(0, number)
    ax.set_ylim(0, int(1.07 * number))
    text = ax.text(0.02, 0.95, "", transform=ax.transAxes)
    iteration = [0]
    def update_fig(arr, rects, iteration):
        for rect, val in zip(rects, arr):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text("# of operations: {}".format(iteration[0]))

    anim = animation.FuncAnimation(fig, func=update_fig, fargs=(bar_rects, iteration),
                                   frames=generator, interval=1, repeat=False)
    plt.show()


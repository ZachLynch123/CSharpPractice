# bubble sort :D 
# big O notation of O(n^2) quadratic time complexity
# For loops inside of for loops are usually n^2

# for merge sort

items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def bubbleSort(dataset):
    # TODO: start with array length and decrement each time
    for i in range(len(dataset)- 1, 0, -1):
        for j in range(i):
            if (dataset[j] > dataset[j+1]):
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
            print("Current state: ", dataset)


# merge sorting O(n log n) (linear time complexity)

def mergesort(dataset):
    # As long as the dataset has more than 1 element, it will keep breaking down

    if len(dataset) > 1:
        mid = len(dataset) // 2
        leftarr = dataset[:mid]
        rightarr = dataset[mid:]

        # TODO:  recursively break down arrays
        mergesort(leftarr)
        mergesort(rightarr)

        # TODO: perform merging

        i = 0 # Index of left array
        j = 0 # Index of right array
        k = 0 # Index of merged array

        # TODO: While both arrays have content
        while (i < len(leftarr) and j < len(rightarr)):
            # if left array is smaller than right. if so join merged array 
            # else join right side to merged array
            if leftarr[i] < rightarr[i]:
                dataset[k] = leftarr[i]
                i += 1
            else: 
                dataset[k] = rightarr[j]
                j += 1
            k += 1
        while (i < len(leftarr)):
            dataset[k] = leftarr[i]
            i += 1
            k += 1
        while(j < len(rightarr)):
            dataset[k] = rightarr[j]
            j += 1
            k += 1

def main():
    list1 = [6, 20, 8, 19, 56, 27, 87, 49, 53]
    print(items)
    mergesort(items)
    print(items)
    # bubbleSort(list1)
    # print("Result: ", list1)

if __name__ == "__main__":
    main()
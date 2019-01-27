# bubble sort :D 
# big O notation of O(n^2) quadratic time complexity
# For loops inside of for loops are usually n^2

def bubbleSort(dataset):
    # TODO: start with array length and decrement each time
    for i in range(len(dataset)- 1, 0, -1):
        for j in range(i):
            if (dataset[j] > dataset[j+1]):
                temp = dataset[j]
                dataset[j] = dataset[j+1]
                dataset[j+1] = temp
            print("Current state: ", dataset)



def main():
    list1 = [6, 20, 8, 19, 56, 27, 87, 49, 53]
    bubbleSort(list1)
    print("Result: ", list1)

if __name__ == "__main__":
    main()
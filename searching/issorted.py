# determine if a list is sorted

itemsOrdered = [6, 8, 19, 20, 23, 49, 87]
itemsUnordered = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def isSorted(itemList):
    # Use brute force method
    for i in range(0, len(itemList)-1):
        if (itemList[i] > itemList[i+1]):
            return False

    return True












print(isSorted(itemsOrdered))
print(isSorted(itemsUnordered))
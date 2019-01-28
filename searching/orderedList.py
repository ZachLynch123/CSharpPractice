# binary search
items = [6, 8, 19, 20, 23, 49, 87]


def binarySearch(item, itemList):
    # get list size
    listSize = len(itemList) - 1
    # start at the two ends of the list
    lowInx = 0
    upInx = listSize

    while lowInx <= upInx:
        # calc midpoint
        midPt = (lowInx + upInx) // 2

        # if found return index
        if itemList[midPt] == item:
            return midPt

        # otherwise get next midpoint
        if item > itemList[midPt]:
            lowInx = midPt + 1
        else: 
            upInx = midPt - 1
    
    if lowInx > upInx:
        return None

print(binarySearch(23, items))
print(binarySearch(87, items))
print(binarySearch(2323, items))
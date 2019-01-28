# Searching for item in unordered list
# Also called linear search
items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def find_item(item, itemList):
    for i in range(0, len(itemList)):
        if item == itemList[i]:
            return i
    return None


print(find_item(87, items))
print(find_item(8723, items))
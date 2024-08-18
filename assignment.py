list_data = [1, 5, 9, 0, 6, 89, 1203, 4, 23]
list_data.sort()
print(list_data)
list_data = [1, 5, 9, 0, 6, 89, 1203, 4, 23]


n = len(list_data)
for i in range(n):
    
    swapped = False
    
    for j in range(0, n - i - 1):
        if list_data[j] > list_data[j + 1]:
        
            list_data[j], list_data[j + 1] = list_data[j + 1], list_data[j]
            swapped = True
    
    if not swapped:
        break

print(list_data)



numbers = [10, 20, 30, 40, 50, 60, 70]

key = int(input("Enter the element to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == key:
        print("Element found at position", mid + 1)
        found = True
        break

    elif key < numbers[mid]:
        high = mid - 1

    else:
        low = mid + 1

if found == False:
    print("Element not found")
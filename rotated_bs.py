
def search(a, start, end, key):
    if start > end:
        return -1

    mid = (start + end)/2
    if a[mid] == key:
        return mid

    l = start
    r = end

    # left in order
    if a[start] < a[mid]:
        if key <= a[mid] and key >= a[start]:
            r = mid - 1
        else:
            l = mid + 1

    # right in order
    elif a[mid] < a[start]:
        if key >= a[mid] and key <= a[end]:
            l = mid + 1
        else:
            r = mid - 1

    return search(a, l, r, key)
            

a = map(int, raw_input().split())
key = int(raw_input())

print search(a, 0, len(a) - 1, key)

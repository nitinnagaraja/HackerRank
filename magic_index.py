magic_index = []

def find_magic_index(a, start, end):
    mid = (start + end)/2

    if start < 0 or end > len(a) - 1 or start > end:
        return

    if mid == a[mid]:
        magic_index.append(mid)

    l = min(mid - 1, a[mid])
    r = max(mid + 1, a[mid])

    find_magic_index(a, start, l)
    find_magic_index(a, r, end)

a = map(int, raw_input().split())

find_magic_index(a, 0, len(a) - 1)

print magic_index

def largest_contiguous_sum(input_list):
    smallest = 0
    largest_sum = float('-inf')
    sum = 0
    for x in input_list:
        sum += x
        if sum < smallest:
            smallest = sum
            partial_sum = sum - smallest
            if partial_sum > largest_sum:
                largest_sum = partial_sum

    return largest_sum

l = [1, 1, 1, -1, 1, -1, -1, -1]

print largest_contiguous_sum(l)

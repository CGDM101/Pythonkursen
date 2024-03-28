# TASK 1 - LIST FUNCTION


# Write a function that takes three arguments: integer A, integer B, and list of integers L. The function must be named in_range. The function must return a new list that contains positions of all elements in list L such that:

#       A <= L[i] <= B

# The function must also raise a ValueError if list L is empty. The error message must contain words "list" and "empty".

# Write a function that returns a list with positions of all numbers in the input list that fall within range ≥ left and ≤ right



# Below is an example of the function usage

# a = 10
# b = 12
# l = [56, -3, 10, 11, 1098, 12, 2]
# in_range(a, b, l)   #[2, 3, 5]


# a = 0
# b = 5
# l =[9, 10, 2, 16, 1, 12, 4, 15, 7, 18, 3, 8, 13, 5, 17]
# in_range(a, b, l)   #[2, 4, 6, 10, 13]


def in_range(left, right, in_list):
    if len(in_list) == 0:
        raise ValueError('The list is empty')
    new_list = []
    for i in range(len(in_list)):
        if in_list[i] >= left and in_list[i] <= right:
            # print(i)
            new_list.append(i)
    return new_list




if __name__ == '__main__':
    my_list = [56, -3, 10, 11, 1098, 12, 2]
    in_left = 10
    in_right = 12
    print(in_range(in_left, in_right, my_list))


if __name__ == '__main__':
    my_list = [4, 3, 7, 9, 1, 0, 1, 6, 2, 8, 4, 2, 4]
    in_left = 2
    in_right = 5
    print(in_range(in_left, in_right, my_list))

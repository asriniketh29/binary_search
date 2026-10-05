'''
All of the functions in this file are classic leetcode style interview questions.
They all take a container xs as input and run in time O(log n),
where n is the length of xs.

JOKE: There are 2 hard problems in computer science:
1. cache invalidation,
2. naming things, and
3. off-by-1 errors.

It's really easy to have off-by-1 errors in these problems.
Pay very close attention to your list indexes and your < vs <= operators.
'''


def find_smallest_positive(xs):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the smallest positive number.
    If no such index exists, return `None`.

    HINT:
    This is essentially the binary search algorithm from class,
    but you're always searching for 0.

    >>> find_smallest_positive([-3, -2, -1, 0, 1, 2, 3])
    4
    >>> find_smallest_positive([1, 2, 3])
    0
    >>> find_smallest_positive([-3, -2, -1]) is None
    True
    '''
    left = 0
    right = len(xs) - 1
    result = None

    while left <= right:
        mid = (left + right) // 2

        if xs[mid] > 0:
            result = mid       # Found a positive number; record index and check left side for a smaller one
            right = mid - 1
        else:
            left = mid + 1     # xs[mid] is <= 0; search in the right half

    return result


def find_largest_negative(xs, lo=0, hi=None):
    '''
    Assume that xs is a list of numbers sorted from LOWEST to HIGHEST.
    Find the index of the largest negative number.
    If no such index exists, return `None`.

    HINT:
    This is the mirror image of find_smallest_positive:
    both functions search for the boundary at 0,
    but they return different sides of that boundary.

    >>> find_largest_negative([-3, -2, -1, 0, 1, 2, 3])
    2
    >>> find_largest_negative([1, 2, 3]) is None
    True
    >>> find_largest_negative([-3, -2, -1])
    2
    '''
    if hi is None:
        hi = len(xs) - 1

    left = lo
    right = hi
    result = None

    while left <= right:
        mid = (left + right) // 2

        if xs[mid] < 0:
            result = mid       # Found a negative number; record index and check right side for a larger one
            left = mid + 1
        else:
            right = mid - 1    # xs[mid] is >= 0; search in the left half

    return result


def find_smallest(xs, lo=0, hi=None):
    '''
    Assume that xs is a list of numbers that is strictly decreasing
    and then strictly increasing,
    so that xs has a unique smallest element.
    Return the index of that element, or `None` if xs is empty.

    NOTE:
    This is the discrete analogue of argmin in src/argmin.py:
    argmin minimizes a convex function over the reals,
    and find_smallest minimizes a list of numbers.

    >>> find_smallest([4, 3, 2, 1, 2, 3])
    3
    >>> find_smallest([1, 2, 3])
    0
    >>> find_smallest([3, 2, 1])
    2
    >>> find_smallest([]) is None
    True
    '''
    if not xs:
        return None

    left, right = 0, len(xs) - 1

    while left < right:
        mid = (left + right) // 2

        # If the element at mid is strictly greater than the element to its right,
        # the minimum must lie strictly to the right.
        if xs[mid] > xs[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left


def count_repeats(xs, x):
    '''
    Assume that xs is a list of numbers sorted from HIGHEST to LOWEST,
    and that x is a number.
    Calculate the number of times that x occurs in xs.

    HINT:
    Use the following three step procedure:
        1) use binary search to find the lowest index with a value >= x
        2) use binary search to find the lowest index with a value < x
        3) return the difference between step 1 and 2
    I highly recommend creating stand-alone functions for steps 1 and 2,
    and write your own doctests for these functions.
    Then, once you're sure these functions work independently,
    completing step 3 will be easy.

    >>> count_repeats([5, 4, 3, 3, 3, 3, 3, 3, 3, 2, 1], 3)
    7
    >>> count_repeats([3, 2, 1], 4)
    0
    '''
    def lowest_index_gte(target):
        # Lowest index where xs[i] <= target in descending order
        left, right = 0, len(xs)
        while left < right:
            mid = (left + right) // 2
            if xs[mid] <= target:
                right = mid
            else:
                left = mid + 1
        return left

    def lowest_index_lt(target):
        # Lowest index where xs[i] < target in descending order
        left, right = 0, len(xs)
        while left < right:
            mid = (left + right) // 2
            if xs[mid] < target:
                right = mid
            else:
                left = mid + 1
        return left

    # Step 1 & Step 2:
    start_index = lowest_index_gte(x)
    end_index = lowest_index_lt(x)

    # Step 3: Return the difference
    return end_index - start_index

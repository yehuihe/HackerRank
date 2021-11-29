from collections.abc import Sequence
from math import ceil


def binary_search(A, n, T):
    """Binary Search algorithm.

    Binary search, also known as half-interval search, logarithmic search,
    or binary chop, is a search algorithm that finds a position of a target
    value within a sorted array.

    Parameters
    ----------
    A : array-like of shape (, n)
        The input sorted array.

    n : int
        The length of A.

    T : int
        The target value.

    Returns
    -------
    index : int or None
        int if target was found else none.

    Notes
    -----
    This iterative procedure keeps track of the search
    boundaries with the two variables L and R.

    In case of duplicate elements. Always return index of
    the leftmost element.

    References
    ----------
    Knuth, Donald. §6.2.1 ("Searching an ordered table"), subsection
        "Algorithm B" (1998)

    Lin, Anthony.
        "Binary search algorithm." WikiJournal of Science, 2019, 2(1):5
        doi: 10.15347/wjs/2019.005 Encyclopedic Review Article
    """
    if not isinstance(A, Sequence) or isinstance(A, str):
        raise ValueError('input A must be a sequence')
    if n < 0:
        raise ValueError('length of the array must be non-negative')

    L = 0
    R = n - 1
    while L <= R:
        m = (L + R) // 2
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            return m
    return None


def binary_search_alternative(A, n, T):
    """Hermann Bottenbruch's Implementation of Binary Search algorithm

    Parameters
    ----------
    A : array-like of shape (, n)
        The input sorted array.

    n : int
        The length of A.

    T : int
        The target value.

    Returns
    -------
    index : int or None
        int if target was found else none.

    Notes
    -----
    In the binary_search procedure, the algorithm checks whether
    the middle element (m) is equal to the target (T) in
    every iteration. Some implementations leave out this
    check during each iteration. The algorithm would perform this check only
    when one element is left (when L = R). This results in a faster comparison
    loop, as one comparison is eliminated per iteration.
    However, it requires one more iteration on average.

    In case of duplicate elements. Always return index of
    the rightmost element.

    References
    ----------
    Willams, Jr., Louis F. A modification to the half-interval
        search (binary search) method. Proceedings of the 14th ACM Southeast
        Conference. ACM. pp. 95–101. doi:10.1145/503561.503582. Retrieved 29
        June 2018. (22 April 1976)

    Knuth, Donald. §6.2.1 ("Searching an ordered table"), subsection
        "History and bibliography" (1998)

    Lin, Anthony.
        "Binary search algorithm." WikiJournal of Science, 2019, 2(1):5
        doi: 10.15347/wjs/2019.005 Encyclopedic Review Article
    """
    if not isinstance(A, Sequence) or isinstance(A, str):
        raise ValueError('input A must be a sequence')
    if n < 0:
        raise ValueError('length of the array must be non-negative')

    L = 0
    R = n - 1
    while L != R:
        m = ceil((L + R) / 2)
        if A[m] > T:
            R = m - 1
        else:
            L = m
    if A[L] == T:
        return L
    return None


def binary_search_duplicate(A, n, T, method='leftmost'):
    """Binary Search algorithm with duplicate elements modification

    Parameters
    ----------
    A : array-like of shape (, n)
        The input sorted array.

    n : int
        The length of A.

    T : int
        The target value.

    method : {'leftmost', 'rightmost'}, default='leftmost'
        Return index position in case of duplicated elements


    Returns
    -------
    index : int or None
        If method="leftmost":

        If L < n and A[L] = T, then A[L] is the leftmost element that equals T.
        Even if T is not in the array, L is the rank of L in the array,
        or the number of elements in the array that are less than T.

        If method="rightmost":

        If L > 0 and A[L-1] = T then A[L-1] is the rightmost element that equals T.
        Even if T is not in the array, (n-1)-L is the number of elements
        in the array that are greater than T.

    Notes
    -----
    The procedure may return any index whose element isequal to the
    target value, even if there are duplicate elements in the array.

    References
    ----------
    Lin, Anthony.
        "Binary search algorithm." WikiJournal of Science, 2019, 2(1):5
        doi: 10.15347/wjs/2019.005 Encyclopedic Review Article
    """
    if not isinstance(A, Sequence) or isinstance(A, str):
        raise ValueError('input A must be a sequence')
    if n < 0:
        raise ValueError('length of the array must be non-negative')
    if method not in ['leftmost', 'rightmost']:
        raise ValueError('method must either be leftmost or rightmost')

    L = 0
    R = n
    if method == 'leftmost':
        while L < R:
            m = (L + R) // 2
            if A[m] < T:
                L = m + 1
            else:
                R = m
        return L
    else:
        while L < R:
            m = (L + R) // 2
            if A[m] > T:
                R = m
            else:
                L = m + 1
        return L - 1


if __name__ == '__main__':
    # A = [1, 2, 3, 4, 4, 5, 6, 7]  # duplicated case
    # A = [3, 5, 1, 4, 2, 6]          # unordered case
    # A = [1, 2, 3, 4, 7, 8, 10, 11, 13, 14, 15]
    A = [80, 90, 100]

    T = 105
    # result = binary_search(A, len(A), T)
    result = binary_search_duplicate(A, len(A), T, method='leftmost')
    print("result: %s" % result)

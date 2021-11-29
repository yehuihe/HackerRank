from collections.abc import Sequence

from .binary_search import (binary_search,
                            binary_search_alternative,
                            binary_search_duplicate)


def rank(A, n, T):
    """Find the number of smaller elements

    Extend binary search to perform approximate matches
    because binary search operates on sorted arrrays.

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
    num : int
        The number of elements less than the target value

    Notes
    -----
    Rank queries can be performed with the procedure for finding the leftmost
    element. The number of el-ements less than the target value
    is returned by the procedure.
    """
    return binary_search_duplicate(A, n, T)


def predecessor(A, n, T):
    """Find next-smallest element

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
    predecessor : int
        Next smallest value.

    Notes
    -----
    Predecessor queries can be performed with rank queries.
    If the rank of the target value is r, its predecessor is r-1.
    """
    return rank(A, n, T) - 1


def successor(A, n, T):
    """Find next-largest element

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
    successor : int
        Next largest value.

    Notes
    -----
    For successor queries, the procedure for finding the rightmost element
    can be used. If the result of running the procedure for the target value
    is r, its predecessor is r+1.

    References
    ----------
    Lin, Anthony.
        "Binary search algorithm." WikiJournal of Science, 2019, 2(1):5
        doi: 10.15347/wjs/2019.005 Encyclopedic Review Article
    """
    return binary_search_duplicate(A, n, T, method='rightmost') + 1


def nearest_neighbor(A, n, T):
    """Find nearest neighbor of the target value

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
    nearest_neighbor : int
        Target value's predecessor or successor, whichever is closer.

    References
    ----------
    Lin, Anthony.
        "Binary search algorithm." WikiJournal of Science, 2019, 2(1):5
        doi: 10.15347/wjs/2019.005 Encyclopedic Review Article
    """



if __name__ == '__main__':
    pass
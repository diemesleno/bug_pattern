#!/usr/bin/env python2

import sys

if sys.version_info >= (3, 0):
	def xrange(*args, **kwargs):
		""" 
        If using with Python 3, the xrange will
        use the range function.
		"""
		return iter(range(*args, **kwargs))


def to_matrix(file_path):
    """
    Get a file and transform it in
    a tuple with a matrix of characters.

    :param file_path: the path to the file

    :return tuple: with the matrix of characters
    """
    with open(file_path) as fobj:
        lines = tuple(line.strip('\n') for line in fobj.readlines())

    longest = max(len(line) for line in lines)
    # Creates a generator with a square matrix of characters with the size of the longest line
    pattern = (tuple(char for char in line.ljust(longest)) for line in lines)

    return tuple(pattern)


def count_pattern(needle_file, haystack_file):
    """
    Search one matrix inside another, computing the indexes of lines
    and columns needed to try each subset with the same size of the
    'needle' (the bug pattern) inside of 'haystack' (the bigger matrix)

    :param needle_file: file with the pattern
    :param haystack_file: The path to the file with the occurrences to find and count based
    in the pattern

    :return int: The number of the pattern occurrences inside the file
    """
    needle, haystack = to_matrix(needle_file), to_matrix(haystack_file)
    needle_rows, haystack_rows = len(needle), len(haystack)
    needle_columns, haystack_columns = len(needle[0]), len(haystack[0])
    count = 0

    column_indexes = tuple(
        (index, index + needle_columns)
        # Change from range to xrange because in Python2 the range function pre-create all elements in memory
        for index in xrange(0, haystack_columns - needle_columns + 1)
    )

    row_indexes = tuple(
        (index, index + needle_rows)
        # Change from range to xrange because in Python2 the range function pre-create all elements in memory
        for index in xrange(0, haystack_rows - needle_rows + 1)
    )

    for row_start, row_end in row_indexes:
        for column_start, column_end in column_indexes:
            subset = tuple(
                row[column_start:column_end]
                for row in haystack[row_start:row_end]
            )
            if needle == subset:
                count += 1

    return count


if __name__ == '__main__':
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("--bug", required=True, help="Bug Pattern File Path")
    ap.add_argument("--land", required=True, help="Landscape File Path")
    args = vars(ap.parse_args())

    print(count_pattern(args["bug"], args["land"]))

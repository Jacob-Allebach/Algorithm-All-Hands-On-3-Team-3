"""Define the name for the approach for performing list sorting with different algorithms."""

from enum import Enum


class AllhandsApproach(str, Enum):
    """Define the name for the approach for performing list sorting with different algorithms."""

    BUBBLESORT = "bubble"
    INSERTIONSORT = "insertion"
    MERGESORT = "merge"
    QUICKSORT = "quick"
    TIMSORT = "tim"
    SELECTION = "selection"
    HEAPSORT = "heap"
    SHELLSORT = "shell"
    RADIX = "radix"
    BUCKET = "bucket"

    def __str__(self):
        """Define a default string representation."""
        return self.value

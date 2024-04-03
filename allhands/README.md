# Algorithm All Hands On 3

## 🔬 Tool Support for Evaluating the Performance of Sorting Algorithms

How to add a new sorting algoritm:

1. Open the sorting.py file.
2. Add the sorting algorithm function with a name ending in _sort to the bottom of the file, accepting an array as a parameter.
3. Open the approach.py file.
4. Integrate the new sorting algorithm as an option.

How to run the tool:

1. cd into the `allhands` directory
2. Enter the devenv shell
3. poetry install all dependencies (I might have to add some dependencies)
4. Run the command `poetry run allhands --starting-size [int] --number-doubles [int]` where starting-size and number-doubles are set to integer

# Algorithm All Hands On 3

This project is a benchmarking tool to assess the efficiency of sorting algorithms by running a doubling experiment.
The tool functions by taking in the name of a Python file, the name of a function within that file, and the parameters
for running the doubling experiment on the function. It will output a table of data showing the results of each run
and a graph of the collected data.

## How to Use Benchmarking Tool

* Navigate into the first `allhands` directory from a terminal window
* Use `devenv shell` to enter a virtual environment with the appropriate Poetry and Python versions
* Use `poetry install` to install all other relevant dependencies into the virtual environment
* Run the benchmarking tool by running a command using the format `poetry run allhands --starting-size [int] --number-doubles [int] --file [str] --function-name [str]` replacing `[int]` and `[str]` with the appropriate variables

"""Conduct doubling experiments for provided algorithms that perform list sorting."""

from timeit import repeat
from typing import Any, List, Tuple

from allhands import generate


def run_sorting_algorithm(
    algorithm: str, array: List[int]
) -> Tuple[str, str, str]:
    """Run a sorting algorithm and profile it with the timeit package."""
    setup_code = f"from allhands.sorting import {algorithm}"
    stmt = f"{algorithm}({array})"
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
    return (min(times)), max(times), (sum(times) / len(times))


def run_sorting_algorithm_experiment_campaign(
    algorithm: str,
    starting_size: int,
    number_doubles: int,
) -> List[List[Any]]:
    """Run an entire sorting algorithm experiment campaign."""
    data_table = []
    while number_doubles > 0:
        random_list = generate.generate_random_container(starting_size)
        performance_data = run_sorting_algorithm(algorithm, random_list)
        data_table_row = [
            starting_size,
            performance_data[0],
            performance_data[1],
            performance_data[2],
        ]
        data_table.append(data_table_row)
        number_doubles = number_doubles - 1
        starting_size = starting_size * 2
    return data_table

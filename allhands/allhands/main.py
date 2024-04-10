import plotly.graph_objs as go
import typer
from plotly.subplots import make_subplots
from rich.console import Console
from tabulate import tabulate

from allhands import approach, benchmark, generate

cli = typer.Typer()
console = Console()


def execute_function(file, function_name, arg):
    with open(file) as f:
        exec(f.read(), globals())
        return globals().get(function_name, lambda _: None)(arg)


# start: The code between the "start" and "end" is a configuration of the tool that runs all sorting algorithms defined in sorting.py at the same time. This configuration does utilize the apporach import so please do not remove this import even if ruff wants to remove it.
# since it runs all algorithms you do not need to have the file or function_name parameter so the command to run this will look something like this: `poetry run allhands --starting-size 100 --number-doubles 5`.
# @cli.command()
# def RunAllAlgorithms(
#     starting_size: int = typer.Option(100),
#     number_doubles: int = typer.Option(5),
# ) -> None:
#     """Conduct a doubling experiment to measure the performance of list sorting for various algorithms."""
#     console.print(
#         "\n🔬 Tool Support for Evaluating the Performance of Sorting Algorithms\n"
#     )
#     console.print(f"Starting size of the data container: {starting_size}\n")
#     console.print(f"Number of doubles to execute: {number_doubles}\n")
#     console.print("📈 Here are the results from running the experiment!\n")

#     approaches = list(approach.AllhandsApproach)
#     all_results = []

#     for approach_enum in approaches:
#         algorithm = f"{approach_enum.value}_sort"
#         max_times = []

#         for i in range(number_doubles):
#             size = starting_size * (2**i)
#             performance_data = benchmark.run_sorting_algorithm(
#                 algorithm, generate.generate_random_container(size)
#             )
#             max_time = max(performance_data)
#             max_times.append(float(max_time))

#         all_results.append(max_times)

#     header = ["Input Size"] + [approach.value for approach in approaches]
#     data = [
#         [starting_size * (2**i)] + [results[i] for results in all_results]
#         for i in range(number_doubles)
#     ]

#     table = tabulate(
#         data, headers=header, tablefmt="fancy_grid", floatfmt=".5f"
#     )
#     console.print(table)

#     # plot
#     fig = make_subplots(rows=1, cols=1)

#     for i, approach_enum in enumerate(approaches):
#         trace = go.Scatter(
#             x=[starting_size * (2**i) for i in range(number_doubles)],
#             y=all_results[i],
#             mode="lines+markers",
#             name=approach_enum.value,
#         )
#         fig.add_trace(trace)

#     fig.update_layout(
#         title="Evaluating the Performance of Sorting Algorithms",
#         xaxis_title="Input Size",
#         yaxis_title="Execution Time (s)",
#         showlegend=True,
#         margin=dict(l=20, r=20, t=60, b=20),
#         title_x=0.5,
#     )

#     fig.show()
# end



# start: The code between the "start" and "end" is a configuration of the tool that runs the sorting algorithms called by the file and function_name parameters.
# since it a single algorithms defined by the file and function_name parameters, the command to run this will look something like this: `poetry run allhands --starting-size 100 --number-doubles 5 --file ./allhands/sorting.py --function-name bubble_sort`.
@cli.command()
def allhands(
    starting_size: int = typer.Option(100),
    number_doubles: int = typer.Option(5),
    file: str = typer.Option("./allhands/sorting.py"),
    function_name: str = typer.Option("bubble_sort"),
) -> None:
    """Conduct a doubling experiment to measure the performance of list sorting for various algorithms."""
    console.print(
        "\n🔬 Tool Support for Evaluating the Performance of Sorting Algorithms\n"
    )
    console.print(f"Starting size of the data container: {starting_size}\n")
    console.print(f"Number of doubles to execute: {number_doubles}\n")
    console.print("📈 Here are the results from running the experiment!\n")

    all_results = []

    for i in range(number_doubles):
        size = starting_size * (2**i)
        data_to_sort = generate.generate_random_container(size)
        performance_data = benchmark.run_sorting_algorithm(
            function_name, data_to_sort
        )
        max_time = max(performance_data)
        max_times = [float(max_time)]

        execute_function(file, function_name, data_to_sort)

        all_results.append(max_times)

    header = ["Input Size", function_name]
    data = [
        [starting_size * (2**i), results[0]]
        for i, results in enumerate(all_results)
    ]

    table = tabulate(
        data, headers=header, tablefmt="fancy_grid", floatfmt=".5f"
    )
    console.print(table)

    # plot
    fig = make_subplots(rows=1, cols=1)

    trace = go.Scatter(
        x=[starting_size * (2**i) for i in range(number_doubles)],
        y=[results[0] for results in all_results],
        mode="lines+markers",
        name=function_name,
    )
    fig.add_trace(trace)

    fig.update_layout(
        title=f"Evaluating the Performance of {function_name}",
        xaxis_title="Input Size",
        yaxis_title="Execution Time (s)",
        showlegend=True,
        margin=dict(l=20, r=20, t=60, b=20),
        title_x=0.5,
    )

    fig.show()
# end

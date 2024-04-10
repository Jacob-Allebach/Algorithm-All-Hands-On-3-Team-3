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
        [starting_size * (2**i), results[0]] for i, results in enumerate(all_results)
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

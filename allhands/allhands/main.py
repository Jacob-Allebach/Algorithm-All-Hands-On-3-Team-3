import plotly.graph_objs as go
import typer
from plotly.subplots import make_subplots
from rich.console import Console
from tabulate import tabulate

from allhands import approach, benchmark, generate

cli = typer.Typer()
console = Console()


@cli.command()
def allhands(
    starting_size: int = typer.Option(100),
    number_doubles: int = typer.Option(5),
) -> None:
    """Conduct a doubling experiment to measure the performance of list sorting for various algorithms."""
    console.print(
        "\n🔬 Tool Support for Evaluating the Performance of Sorting Algorithms\n"
    )
    console.print(f"Starting size of the data container: {starting_size}\n")
    console.print(f"Number of doubles to execute: {number_doubles}\n")
    console.print("📈 Here are the results from running the experiment!\n")

    approaches = list(approach.AllhandsApproach)
    all_results = []

    for approach_enum in approaches:
        algorithm = f"{approach_enum.value}_sort"
        max_times = []

        for i in range(number_doubles):
            size = starting_size * (2**i)
            performance_data = benchmark.run_sorting_algorithm(
                algorithm, generate.generate_random_container(size)
            )
            max_time = max(performance_data)
            max_times.append(float(max_time))

        all_results.append(max_times)

    header = ["Input Size"] + [approach.value for approach in approaches]
    data = [
        [starting_size * (2**i)] + [results[i] for results in all_results]
        for i in range(number_doubles)
    ]

    table = tabulate(
        data, headers=header, tablefmt="fancy_grid", floatfmt=".5f"
    )
    console.print(table)

    # plot
    fig = make_subplots(rows=1, cols=1)

    for i, approach_enum in enumerate(approaches):
        trace = go.Scatter(
            x=[starting_size * (2**i) for i in range(number_doubles)],
            y=all_results[i],
            mode="lines+markers",
            name=approach_enum.value,
        )
        fig.add_trace(trace)

    fig.update_layout(
        title="Evaluating the Performance of Sorting Algorithms",
        xaxis_title="Input Size",
        yaxis_title="Execution Time (s)",
        showlegend=True,
        margin=dict(l=20, r=20, t=60, b=20),
        title_x=0.5,
    )

    fig.show()

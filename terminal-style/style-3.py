from rich import box
from rich.console import Console
from rich.panel import Panel

console = Console()

p1 = Panel(
    'Do you really want it?',
    title='Confirmation',
    subtitle='Type yes or no...',
    box=box.DOUBLE_EDGE,
    padding=1,
    style='red'
)

console.print()

console.print(p1)

console.print()
console.input('([green]Yes[/]/[red]No[/]) ')

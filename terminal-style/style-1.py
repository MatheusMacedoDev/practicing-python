from rich import print as rprint
from rich.style import Style
from rich.console import Console

import time

print([1, 2, 3, 4, 5])
rprint([1, 2, 3, 4, 5])

rprint('[red]Matheus[/red] Macedo Santos')
rprint('Matheus [blue]Macedo[/blue] Santos')
rprint('Matheus Macedo [magenta]Santos[/magenta]')

console = Console()

danger_style = Style(color='red', italic=True, bold=True, blink2=True, underline=True)
console.print("Super [link=https://youtube.com]Alerta[/link] Radical", style=danger_style)

console.log('Hello, world')
console.print('FOO', style='red on white')
console.print_json('[false, true, null, "foo"]')

console.rule('[bold red]Level 1')

with console.status('Working...'):
    time.sleep(1)

console.print('Rich', justify='center')
console.print('Rich', justify='center', style='blink bold frame overline #F5E818 on white')
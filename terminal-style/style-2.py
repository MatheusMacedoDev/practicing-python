from rich import inspect
from rich.console import Console
from rich.theme import Theme

custom_theme = Theme({
    'matheus': 'red'
})

console = Console(theme=custom_theme)

console.print('[matheus]Macedo[/matheus]')

class Obj:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

inspect(Obj("Matheus", 18, 173))
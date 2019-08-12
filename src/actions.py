from typing import Callable

class Action():

    def __init__(self, selection: str, name: str, action: Callable[[], None]):
        self.selection = selection
        self.name = name
        self.action = action

    def __str__(self) -> str:
        return f'{self.selection}: {self.name}'

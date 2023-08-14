
class ConsoleStub:
    def __init__(self) -> None:
        self.prints = []

    def print(self, content: str) -> None:
        self.prints.append(content)

from dataclasses import dataclass


@dataclass
class Number:
    value: int | float

    def __repr__(self):
        return str(self.value)

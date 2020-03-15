from typing import List

from . import MovementLine, Header, Footer


class Norma43Document:
    def __init__(self, header: Header = None, movement_lines: List[MovementLine] = [], footer: Footer = None):
        self.header = header
        self.movement_lines = movement_lines
        self.footer = footer

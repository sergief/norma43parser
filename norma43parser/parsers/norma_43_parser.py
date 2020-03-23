from typing import Final

from .line_parser_factory import LineParserFactory
from .line_type import LineType
from ..models import Norma43Document


class Norma43Parser:
    def __init__(self, date_format: str = "DMY"):
        self.DATE_FORMAT: Final[str] = date_format

    def parse(self, content: str) -> Norma43Document:
        norma_43 = Norma43Document()

        for line in content.splitlines():
            norma_43 = LineParserFactory.get_instance(LineType.get_line_type(line)).parse(
                line, norma_43, self.DATE_FORMAT
            )

        return norma_43

import copy

from .line_parser import LineParser
from .. import Norma43Document


class EndOfFileParser(LineParser):
    @classmethod
    def parse(cls, line: str, norma_43: Norma43Document, date_format: str) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        ret.reported_entries = int(line[20:])
        return ret

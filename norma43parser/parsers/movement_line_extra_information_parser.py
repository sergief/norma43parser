import copy

from .line_parser import LineParser
from .. import Norma43Document


class MovementLineExtraInformationParser(LineParser):
    @classmethod
    def parse(cls, line: str, norma_43: Norma43Document, date_format: str) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        ret.movement_lines[-1].extra_information.append(line[4:])
        return ret

import copy
from enum import Enum

from src.models import Norma43Document


class LineType(Enum):
    HEADER = 11
    MOVEMENT_LINE = 22
    MOVEMENT_LINE_EXTRA_INFORMATION = 23
    FOOTER = 33
    END_OF_FILE = 88


class Norma43Parser:
    @classmethod
    def parse_norma_43_file_contents(cls, content: str) -> Norma43Document:
        norma_43 = Norma43Document()

        for line in content:
            line_type = cls._get_line_type(line)

            if line_type == LineType.HEADER:
                norma_43 = cls._parse_header(line, norma_43)
                continue

            if line_type == LineType.MOVEMENT_LINE:
                norma_43 = cls._parse_movement_line(line, norma_43)
                continue

            if line_type == LineType.MOVEMENT_LINE_EXTRA_INFORMATION:
                norma_43 = cls._parse_movement_line_extra_information(line, norma_43)
                continue

            if line_type == LineType.FOOTER:
                norma_43 = cls._parse_footer(line, norma_43)
                continue

            if line_type == LineType.END_OF_FILE:
                norma_43 = cls._parse_end_of_file(line, norma_43)

        return norma_43

    @classmethod
    def _get_line_type(cls, line: str) -> LineType:
        identifier = int(line[:2])
        return LineType(identifier)

    @classmethod
    def _parse_header(cls, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        # TODO
        return ret

    @classmethod
    def _parse_movement_line(cls, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        # TODO
        return ret

    @classmethod
    def _parse_movement_line_extra_information(cls, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        # TODO
        return ret

    @classmethod
    def _parse_footer(cls, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        # TODO
        return ret

    @classmethod
    def _parse_end_of_file(cls, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        # TODO
        return ret

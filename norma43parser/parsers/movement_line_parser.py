import copy
from decimal import Decimal

from .date_format import DateFormat
from .line_parser import LineParser
from .. import Norma43Document, MovementLine


class MovementLineParser(LineParser):
    @classmethod
    def parse(cls, line: str, norma_43: Norma43Document, date_format: DateFormat) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        branch_key = line[6:10]
        operation_date = cls._retrieve_date(line[10:16], date_format)
        value_date = cls._retrieve_date(line[16:22], date_format)
        initial_balance_sign = 1 if line[27:28] == "2" else -1
        initial_balance_str = line[28:42]
        initial_balance = initial_balance_sign * Decimal(initial_balance_str) / Decimal("100")
        description = line[52:]
        ret.accounts[-1].movement_lines.append(
            MovementLine(
                branch_key=branch_key,
                operation_date=operation_date,
                value_date=value_date,
                initial_balance=initial_balance,
                description=description,
            )
        )
        return ret

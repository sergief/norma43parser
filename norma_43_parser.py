import copy
from datetime import datetime, date
from decimal import Decimal
from enum import Enum
from typing import Final

from models import Norma43Document, Header, Footer, MovementLine


class LineType(Enum):
    HEADER = 11
    MOVEMENT_LINE = 22
    MOVEMENT_LINE_EXTRA_INFORMATION = 23
    FOOTER = 33
    END_OF_FILE = 88


class Norma43Parser:
    def __init__(self, date_format: str = "DMY"):
        self.DATE_FORMAT: Final[str] = date_format

    def parse_norma_43_file_contents(self, content: str) -> Norma43Document:
        norma_43 = Norma43Document()

        for line in content.splitlines():
            line_type = self._get_line_type(line)

            if line_type == LineType.HEADER:
                norma_43 = self._parse_header(line, norma_43)
                continue

            if line_type == LineType.MOVEMENT_LINE:
                norma_43 = self._parse_movement_line(line, norma_43)
                continue

            if line_type == LineType.MOVEMENT_LINE_EXTRA_INFORMATION:
                norma_43 = self._parse_movement_line_extra_information(line, norma_43)
                continue

            if line_type == LineType.FOOTER:
                norma_43 = self._parse_footer(line, norma_43)
                continue

            if line_type == LineType.END_OF_FILE:
                norma_43 = self._parse_end_of_file(line, norma_43)

        return norma_43

    def _get_line_type(self, line: str) -> LineType:
        identifier = int(line[:2])
        return LineType(identifier)

    def _retrieve_date(self, encoded_date: str) -> date:
        year = ""
        month = ""
        day = ""

        i = 0

        for _ in range(len(self.DATE_FORMAT)):
            symbol = self.DATE_FORMAT[i]
            encoded_date_part = encoded_date[i * 2 : i * 2 + 2]
            if symbol == "Y":
                year = "20" + encoded_date_part
            elif symbol == "D":
                day = encoded_date_part
            elif symbol == "M":
                month = encoded_date_part
            i += 1
        return datetime(int(year), int(month), int(day)).date()

    def _parse_header(self, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        bank_identifier = line[2:6]
        branch_key = line[6:10]
        account_number = line[10:20]
        start_date = self._retrieve_date(line[20:26])
        end_date = self._retrieve_date(line[26:32])

        initial_balance_sign = 1 if line[32:33] == "2" else -1
        initial_balance_str = line[33:47]
        initial_balance = initial_balance_sign * Decimal(initial_balance_str) / Decimal("100")
        currency = line[47:50]
        type_of_information_service = line[50:51]
        account_name = line[51:]
        ret.header = Header(
            bank_identifier=bank_identifier,
            branch_key=branch_key,
            account_number=account_number,
            start_date=start_date,
            end_date=end_date,
            initial_balance=initial_balance,
            currency=currency,
            type_of_information_service=type_of_information_service,
            account_name=account_name,
        )
        # TODO replace currency
        return ret

    def _parse_movement_line(self, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        branch_key = line[6:10]
        operation_date = self._retrieve_date(line[10:16])
        value_date = self._retrieve_date(line[16:22])
        initial_balance_sign = 1 if line[27:28] == "2" else -1
        initial_balance_str = line[28:42]
        initial_balance = initial_balance_sign * Decimal(initial_balance_str) / Decimal("100")
        description = line[52:]
        ret.movement_lines.append(
            MovementLine(
                branch_key=branch_key,
                operation_date=operation_date,
                value_date=value_date,
                initial_balance=initial_balance,
                description=description,
            )
        )
        return ret

    def _parse_movement_line_extra_information(self, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        ret.movement_lines[-1].extra_information.append(line[4:])
        return ret

    def _parse_footer(self, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        bank_identifier = line[2:6]
        branch_key = line[6:10]
        account_number = line[10:20]
        debit_entries = int(line[20:24])
        debit_amount = Decimal(line[24:38]) / Decimal("100")
        credit_entries = int(line[38:42])
        credit_amount = Decimal(line[42:56]) / Decimal("100")
        final_balance_sign = 1 if line[56:57] == "2" else -1
        final_balance_str = line[57:71]
        final_balance = final_balance_sign * Decimal(final_balance_str) / Decimal("100")
        currency = line[71:74]
        # TODO: convert currency
        ret.footer = Footer(
            bank_identifier=bank_identifier,
            branch_key=branch_key,
            account_number=account_number,
            debit_entries=debit_entries,
            debit_amount=debit_amount,
            credit_entries=credit_entries,
            credit_amount=credit_amount,
            final_balance=final_balance,
            currency=currency,
        )
        return ret

    def _parse_end_of_file(self, line: str, norma_43: Norma43Document) -> Norma43Document:
        ret = copy.deepcopy(norma_43)
        ret.reported_entries = int(line[20:])
        return ret

from datetime import date, datetime

from norma43parser import Norma43Document


class LineParser:
    @classmethod
    def parse(cls, line: str, norma_43: Norma43Document, date_format: str) -> Norma43Document:
        pass

    @staticmethod
    def _retrieve_date(encoded_date: str, date_format: str) -> date:
        year = ""
        month = ""
        day = ""

        i = 0

        for _ in range(len(date_format)):
            symbol = date_format[i]
            encoded_date_part = encoded_date[i * 2 : i * 2 + 2]
            if symbol == "Y":
                year = "20" + encoded_date_part
            elif symbol == "D":
                day = encoded_date_part
            elif symbol == "M":
                month = encoded_date_part
            i += 1
        return datetime(int(year), int(month), int(day)).date()

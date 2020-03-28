from datetime import date
from decimal import Decimal

from norma43parser import Norma43Document, DateFormat, Account
from norma43parser.parsers.movement_line_parser import MovementLineParser


class TestMovementLineParser:
    @classmethod
    def setup_class(cls):
        cls.CONTENT = "2212342222010218010218011112000000000050250000000000ORDEN PAGO RECIB"

    def test_parse_branch_code(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account()]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].branch_key == "2222"

    def test_parse_operation_date(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account()]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].operation_date == date(2018, 2, 1)

    def test_parse_initial_balance(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account()]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].initial_balance == Decimal("50.25")

    def test_parse_description(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account()]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].description == "ORDEN PAGO RECIB"

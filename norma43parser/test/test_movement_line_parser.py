from datetime import date
from decimal import Decimal

from norma43parser import Norma43Document, DateFormat, Account, Header
from norma43parser.parsers.movement_line_parser import MovementLineParser


class TestMovementLineParser:
    @classmethod
    def setup_class(cls):
        cls.CONTENT = "2212342222010218010218011112000000000050250000000000NEW MAC COMPUTER"

    def test_parse_branch_code(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account(header=Header(initial_balance=0))]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].branch_code == "2222"

    def test_parse_transaction_date(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account(header=Header(initial_balance=0))]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].transaction_date == date(2018, 2, 1)

    def test_parse_amount(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account(header=Header(initial_balance=0))]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].amount == Decimal("50.25")

    def test_parse_description(self):
        norma_43_document = MovementLineParser.parse(
            self.CONTENT, Norma43Document(accounts=[Account(header=Header(initial_balance=0))]), DateFormat.SPANISH
        )
        assert norma_43_document.accounts[0].movement_lines[0].description == "NEW MAC COMPUTER"

from datetime import date
from decimal import Decimal

from norma43parser import Norma43Document, DateFormat
from norma43parser.parsers.header_parser import HeaderParser


class TestHeaderParser:
    @classmethod
    def setup_class(cls):
        cls.HEADER_CONTENT = "111234222212345678900102180202182000000002000009783MI EMPRESA SL 099"

    def test_parse_header_bank_identifier(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.bank_identifier == "1234"

    def test_parse_header_branch_key(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.branch_key == "2222"

    def test_parse_header_account_number(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.account_number == "1234567890"

    def test_parse_header_start_date(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.start_date == date(2018, 2, 1)

    def test_parse_header_start_date_different_format(self):
        header_content = "111234222212345678901802011802022000000002000009783MI EMPRESA SL 099"
        norma_43_document = HeaderParser.parse(header_content, Norma43Document(), DateFormat.ENGLISH)
        assert norma_43_document.header.start_date == date(2018, 2, 1)

    def test_parse_header_end_date(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.end_date == date(2018, 2, 2)

    def test_parse_header_initial_balance(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.initial_balance == Decimal("2000.00")

    def test_parse_header_currency(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.currency == "978"

    def test_parse_type_of_information_service(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.type_of_information_service == "3"

    def test_parse_account_name(self):
        norma_43_document = HeaderParser.parse(self.HEADER_CONTENT, Norma43Document(), DateFormat.SPANISH)
        assert norma_43_document.header.account_name == "MI EMPRESA SL 099"

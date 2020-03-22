from datetime import date
from decimal import Decimal

from norma_43_parser import Norma43Parser


def test_parse_end_of_file():
    line_content = "88999999999999999999123456"
    norma_43_document = Norma43Parser().parse_norma_43_file_contents(line_content)
    assert norma_43_document.reported_entries == 123456


class TestHeaderParser:
    @classmethod
    def setup_class(cls):
        cls.HEADER_CONTENT = "111234222212345678900102180202182000000002000009783MI EMPRESA SL 099"

    def test_parse_header_bank_identifier(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.bank_identifier == "1234"

    def test_parse_header_branch_key(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.branch_key == "2222"

    def test_parse_header_account_number(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.account_number == "1234567890"

    def test_parse_header_start_date(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.start_date == date(2018, 2, 1)

    def test_parse_header_start_date_different_format(self):
        header_content = "111234222212345678901802011802022000000002000009783MI EMPRESA SL 099"

        norma_43_document = Norma43Parser(date_format="YMD").parse_norma_43_file_contents(header_content)
        assert norma_43_document.header.start_date == date(2018, 2, 1)

    def test_parse_header_end_date(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.end_date == date(2018, 2, 2)

    def test_parse_header_initial_balance(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.initial_balance == Decimal("2000.00")

    def test_parse_header_currency(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.currency == "978"

    def test_parse_type_of_information_service(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.type_of_information_service == "3"

    def test_parse_account_name(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.HEADER_CONTENT)
        assert norma_43_document.header.account_name == "MI EMPRESA SL 099"


class TestFooterParser:
    @classmethod
    def setup_class(cls):
        cls.FOOTER_CONTENT = "3312342222123456789000000000000000000000000200000000015075200000000215075978"

    def test_parse_header_bank_identifier(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.bank_identifier == "1234"

    def test_parse_header_branch_key(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.branch_key == "2222"

    def test_parse_header_account_number(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.account_number == "1234567890"

    def test_parse_debit_entries(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.debit_entries == 0

    def test_parse_debit_amount(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.debit_amount == 0

    def test_parse_credit_entries(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.credit_entries == 2

    def test_parse_credit_amount(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.credit_amount == Decimal("150.75")

    def test_parse_final_balance(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.final_balance == Decimal("2150.75")

    def test_parse_currency(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.FOOTER_CONTENT)
        assert norma_43_document.footer.currency == "978"


class TestMovementLineParser:
    @classmethod
    def setup_class(cls):
        cls.CONTENT = """2212342222010218010218011112000000000050250000000000ORDEN PAGO RECIB
2301LIQ. OP. N 000000000000069
2302AUTOMOCION LAGUNA SL 41001 SEVILLA ES"""

    def test_parse_branch_code(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.CONTENT)
        assert norma_43_document.movement_lines[0].branch_key == "2222"

    def test_parse_operation_date(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.CONTENT)
        assert norma_43_document.movement_lines[0].operation_date == date(2018, 2, 1)

    def test_parse_initial_balance(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.CONTENT)
        assert norma_43_document.movement_lines[0].initial_balance == Decimal("50.25")

    def test_parse_description(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.CONTENT)
        assert norma_43_document.movement_lines[0].description == "ORDEN PAGO RECIB"

    def test_parse_extra_information(self):
        norma_43_document = Norma43Parser().parse_norma_43_file_contents(self.CONTENT)
        extra_information = norma_43_document.movement_lines[0].extra_information

        assert len(extra_information) == 2
        assert extra_information[0] == "LIQ. OP. N 000000000000069"
        assert extra_information[1] == "AUTOMOCION LAGUNA SL 41001 SEVILLA ES"

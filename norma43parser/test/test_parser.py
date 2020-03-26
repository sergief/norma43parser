from datetime import date
from decimal import Decimal

from norma43parser import Norma43Parser, DateFormat


class TestParser:
    @classmethod
    def setup_class(cls):
        cls.FILE_CONTENT = """111234222212345678900102180202182000000002000009783MI EMPRESA SL 099
2212342222010218010218011112000000000050250000000000ORDEN PAGO RECIB
2301LIQ. OP. N 000000000000069
2302AUTOMOCION LAGUNA SL 41001 SEVILLA ES
3312342222123456789000000000000000000000000200000000015075200000000215075978
88999999999999999999123456"""
        cls.norma_43_document = Norma43Parser(DateFormat.SPANISH).parse(cls.FILE_CONTENT)

    def test_parse_header_bank_identifier(self):
        assert self.norma_43_document.header.bank_identifier == "1234"

    def test_parse_header_branch_key(self):
        assert self.norma_43_document.header.branch_key == "2222"

    def test_parse_header_account_number(self):
        assert self.norma_43_document.header.account_number == "1234567890"

    def test_parse_header_start_date(self):
        assert self.norma_43_document.header.start_date == date(2018, 2, 1)

    def test_parse_header_end_date(self):
        assert self.norma_43_document.header.end_date == date(2018, 2, 2)

    def test_parse_header_initial_balance(self):
        assert self.norma_43_document.header.initial_balance == Decimal("2000.00")

    def test_parse_header_currency(self):
        assert self.norma_43_document.header.currency == "978"

    def test_parse_header_type_of_information_service(self):
        assert self.norma_43_document.header.type_of_information_service == "3"

    def test_parse_header_account_name(self):
        assert self.norma_43_document.header.account_name == "MI EMPRESA SL 099"

    def test_parse_branch_code(self):
        assert self.norma_43_document.movement_lines[0].branch_key == "2222"

    def test_parse_operation_date(self):
        assert self.norma_43_document.movement_lines[0].operation_date == date(2018, 2, 1)

    def test_parse_initial_balance(self):
        assert self.norma_43_document.movement_lines[0].initial_balance == Decimal("50.25")

    def test_parse_description(self):
        assert self.norma_43_document.movement_lines[0].description == "ORDEN PAGO RECIB"

    def test_parse_extra_information(self):
        extra_information = self.norma_43_document.movement_lines[0].extra_information

        assert len(extra_information) == 2
        assert extra_information[0] == "LIQ. OP. N 000000000000069"
        assert extra_information[1] == "AUTOMOCION LAGUNA SL 41001 SEVILLA ES"

    def test_parse_footer_bank_identifier(self):
        assert self.norma_43_document.footer.bank_identifier == "1234"

    def test_parse_footer_branch_key(self):
        assert self.norma_43_document.footer.branch_key == "2222"

    def test_parse_footer_account_number(self):
        assert self.norma_43_document.footer.account_number == "1234567890"

    def test_parse_footer_debit_entries(self):
        assert self.norma_43_document.footer.debit_entries == 0

    def test_parse_footer_debit_amount(self):
        assert self.norma_43_document.footer.debit_amount == 0

    def test_parse_footer_credit_entries(self):
        assert self.norma_43_document.footer.credit_entries == 2

    def test_parse_footer_credit_amount(self):
        assert self.norma_43_document.footer.credit_amount == Decimal("150.75")

    def test_parse_footer_final_balance(self):
        assert self.norma_43_document.footer.final_balance == Decimal("2150.75")

    def test_parse_footer_currency(self):
        assert self.norma_43_document.footer.currency == "978"

    def test_parse_end_of_file(self):
        assert self.norma_43_document.reported_entries == 123456

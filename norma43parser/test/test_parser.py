import os
from datetime import date
from decimal import Decimal

from norma43parser import Norma43Parser, DateFormat


class TestParserSingleAccount:
    @classmethod
    def setup_class(cls):
        cls.FILE_CONTENT = """111234222212345678900102180202182000000002000009783ACME INC XYZAB
2212342222010218010218011112000000000050250000000000NEW MAC COMPUTER
2301PAYMENT OPERATION APPROVED
2302GROCERIES AND OTHER PAYMENTS SSSLLLAB
3312342222123456789000000000000000000000000200000000015075200000000215075978
88999999999999999999123456"""
        cls.norma_43_document = Norma43Parser(DateFormat.SPANISH).parse(cls.FILE_CONTENT)

    def test_parse_header_bank_identifier(self):
        assert self.norma_43_document.accounts[0].header.bank_identifier == "1234"

    def test_parse_header_branch_key(self):
        assert self.norma_43_document.accounts[0].header.branch_key == "2222"

    def test_parse_header_account_number(self):
        assert self.norma_43_document.accounts[0].header.account_number == "1234567890"

    def test_parse_header_start_date(self):
        assert self.norma_43_document.accounts[0].header.start_date == date(2018, 2, 1)

    def test_parse_header_end_date(self):
        assert self.norma_43_document.accounts[0].header.end_date == date(2018, 2, 2)

    def test_parse_header_initial_balance(self):
        assert self.norma_43_document.accounts[0].header.initial_balance == Decimal("2000.00")

    def test_parse_header_currency(self):
        assert self.norma_43_document.accounts[0].header.currency == "978"

    def test_parse_header_information_mode_code(self):
        assert self.norma_43_document.accounts[0].header.information_mode_code == "3"

    def test_parse_header_account_name(self):
        assert self.norma_43_document.accounts[0].header.account_name == "ACME INC XYZAB"

    def test_parse_branch_code(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].branch_key == "2222"

    def test_parse_operation_date(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].operation_date == date(2018, 2, 1)

    def test_parse_amount(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].amount == Decimal("50.25")

    def test_parse_description(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].description == "NEW MAC COMPUTER"

    def test_parse_extra_information(self):
        extra_information = self.norma_43_document.accounts[0].movement_lines[0].extra_information

        assert len(extra_information) == 2
        assert extra_information[0] == "PAYMENT OPERATION APPROVED"
        assert extra_information[1] == "GROCERIES AND OTHER PAYMENTS SSSLLLAB"

    def test_parse_footer_bank_identifier(self):
        assert self.norma_43_document.accounts[0].footer.bank_identifier == "1234"

    def test_parse_footer_branch_key(self):
        assert self.norma_43_document.accounts[0].footer.branch_key == "2222"

    def test_parse_footer_account_number(self):
        assert self.norma_43_document.accounts[0].footer.account_number == "1234567890"

    def test_parse_footer_debit_entries(self):
        assert self.norma_43_document.accounts[0].footer.debit_entries == 0

    def test_parse_footer_debit_amount(self):
        assert self.norma_43_document.accounts[0].footer.debit_amount == 0

    def test_parse_footer_credit_entries(self):
        assert self.norma_43_document.accounts[0].footer.credit_entries == 2

    def test_parse_footer_credit_amount(self):
        assert self.norma_43_document.accounts[0].footer.credit_amount == Decimal("150.75")

    def test_parse_footer_final_balance(self):
        assert self.norma_43_document.accounts[0].footer.final_balance == Decimal("2150.75")

    def test_parse_footer_currency(self):
        assert self.norma_43_document.accounts[0].footer.currency == "978"

    def test_parse_end_of_file(self):
        assert self.norma_43_document.reported_entries == 123456


class TestParseMultiAccountAccount:
    @classmethod
    def setup_class(cls):
        cls.FILE_CONTENT = """111234222212345678900102180202182000000002000009783ACME INC XYZAB
2212342222010218010218011112000000000050250000000000NEW MAC COMPUTER
2301PAYMENT OPERATION APPROVED
2302GROCERIES AND OTHER PAYMENTS SSSLLLAB
3312342222123456789000000000000000000000000200000000015075200000000215075978
114321444498765432100405200505202000000003000009793EVIL CORPORATI088
2243214444040520040520011112000000000050270000000000CONCEPT PAYMENT1
2301SUCCESSFUL PAYMENT OPERAT.
2302SUPERMARKET AND OTHER PAYMENTS S12345
3343214444987654321000000000000000000000000200000000015175200000000215175979
88999999999999999999123456"""
        cls.norma_43_document = Norma43Parser(DateFormat.SPANISH).parse(cls.FILE_CONTENT)

    def test_parse_header_bank_identifier(self):
        assert self.norma_43_document.accounts[0].header.bank_identifier == "1234"
        assert self.norma_43_document.accounts[1].header.bank_identifier == "4321"

    def test_parse_header_branch_key(self):
        assert self.norma_43_document.accounts[0].header.branch_key == "2222"
        assert self.norma_43_document.accounts[1].header.branch_key == "4444"

    def test_parse_header_account_number(self):
        assert self.norma_43_document.accounts[0].header.account_number == "1234567890"
        assert self.norma_43_document.accounts[1].header.account_number == "9876543210"

    def test_parse_header_start_date(self):
        assert self.norma_43_document.accounts[0].header.start_date == date(2018, 2, 1)
        assert self.norma_43_document.accounts[1].header.start_date == date(2020, 5, 4)

    def test_parse_header_end_date(self):
        assert self.norma_43_document.accounts[0].header.end_date == date(2018, 2, 2)
        assert self.norma_43_document.accounts[1].header.end_date == date(2020, 5, 5)

    def test_parse_header_initial_balance(self):
        assert self.norma_43_document.accounts[0].header.initial_balance == Decimal("2000.00")
        assert self.norma_43_document.accounts[1].header.initial_balance == Decimal("3000.00")

    def test_parse_header_currency(self):
        assert self.norma_43_document.accounts[0].header.currency == "978"
        assert self.norma_43_document.accounts[1].header.currency == "979"

    def test_parse_header_information_mode_code(self):
        assert self.norma_43_document.accounts[0].header.information_mode_code == "3"
        assert self.norma_43_document.accounts[1].header.information_mode_code == "3"

    def test_parse_header_account_name(self):
        assert self.norma_43_document.accounts[0].header.account_name == "ACME INC XYZAB"
        assert self.norma_43_document.accounts[1].header.account_name == "EVIL CORPORATI088"

    def test_parse_branch_code(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].branch_key == "2222"
        assert self.norma_43_document.accounts[1].movement_lines[0].branch_key == "4444"

    def test_parse_operation_date(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].operation_date == date(2018, 2, 1)

    def test_parse_amount(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].amount == Decimal("50.25")
        assert self.norma_43_document.accounts[1].movement_lines[0].amount == Decimal("50.27")

    def test_parse_description(self):
        assert self.norma_43_document.accounts[0].movement_lines[0].description == "NEW MAC COMPUTER"
        assert self.norma_43_document.accounts[1].movement_lines[0].description == "CONCEPT PAYMENT1"

    def test_parse_extra_information(self):
        extra_information = self.norma_43_document.accounts[0].movement_lines[0].extra_information

        assert len(extra_information) == 2
        assert extra_information[0] == "PAYMENT OPERATION APPROVED"
        assert extra_information[1] == "GROCERIES AND OTHER PAYMENTS SSSLLLAB"

        extra_information = self.norma_43_document.accounts[1].movement_lines[0].extra_information
        assert len(extra_information) == 2
        assert extra_information[0] == "SUCCESSFUL PAYMENT OPERAT."
        assert extra_information[1] == "SUPERMARKET AND OTHER PAYMENTS S12345"

    def test_parse_footer_bank_identifier(self):
        assert self.norma_43_document.accounts[0].footer.bank_identifier == "1234"
        assert self.norma_43_document.accounts[1].footer.bank_identifier == "4321"

    def test_parse_footer_branch_key(self):
        assert self.norma_43_document.accounts[0].footer.branch_key == "2222"
        assert self.norma_43_document.accounts[1].footer.branch_key == "4444"

    def test_parse_footer_account_number(self):
        assert self.norma_43_document.accounts[0].footer.account_number == "1234567890"
        assert self.norma_43_document.accounts[1].footer.account_number == "9876543210"

    def test_parse_footer_debit_entries(self):
        assert self.norma_43_document.accounts[0].footer.debit_entries == 0
        assert self.norma_43_document.accounts[1].footer.debit_entries == 0

    def test_parse_footer_debit_amount(self):
        assert self.norma_43_document.accounts[0].footer.debit_amount == 0
        assert self.norma_43_document.accounts[1].footer.debit_amount == 0

    def test_parse_footer_credit_entries(self):
        assert self.norma_43_document.accounts[0].footer.credit_entries == 2
        assert self.norma_43_document.accounts[1].footer.credit_entries == 2

    def test_parse_footer_credit_amount(self):
        assert self.norma_43_document.accounts[0].footer.credit_amount == Decimal("150.75")
        assert self.norma_43_document.accounts[1].footer.credit_amount == Decimal("151.75")

    def test_parse_footer_final_balance(self):
        assert self.norma_43_document.accounts[0].footer.final_balance == Decimal("2150.75")
        assert self.norma_43_document.accounts[1].footer.final_balance == Decimal("2151.75")

    def test_parse_footer_currency(self):
        assert self.norma_43_document.accounts[0].footer.currency == "978"
        assert self.norma_43_document.accounts[1].footer.currency == "979"

    def test_parse_end_of_file(self):
        assert self.norma_43_document.reported_entries == 123456


class TestParseBalance:
    @classmethod
    def setup_class(cls):
        cls.FILE_CONTENT = open(f"{os.path.dirname(__file__)}/fixtures/movements.n43", "r").read()

    def test_balance_values(self):
        norma_43 = Norma43Parser(date_format=DateFormat.SPANISH).parse(self.FILE_CONTENT)

        movement_lines = norma_43.accounts[0].movement_lines

        balances = [
            "2439.44",
            "2369.15",
            "2298.86",
            "2160.29",
            "2159.29",
            "2063.29",
            "1967.29",
            "2467.29",
            "2424.04",
            "2418.89",
            "2414.24",
            "2378.24",
            "2358.93",
            "2332.23",
            "2308.03",
            "2301.59",
        ]
        for line in movement_lines:
            assert line.balance == Decimal(balances.pop(0))

from decimal import Decimal

from norma43parser import Norma43Document
from norma43parser.parsers.footer_parser import FooterParser


class TestFooterParser:
    @classmethod
    def setup_class(cls):
        cls.FOOTER_CONTENT = "3312342222123456789000000000000000000000000200000000015075200000000215075978"

    def test_parse_header_bank_identifier(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.bank_identifier == "1234"

    def test_parse_header_branch_key(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.branch_key == "2222"

    def test_parse_header_account_number(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.account_number == "1234567890"

    def test_parse_debit_entries(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.debit_entries == 0

    def test_parse_debit_amount(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.debit_amount == 0

    def test_parse_credit_entries(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.credit_entries == 2

    def test_parse_credit_amount(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.credit_amount == Decimal("150.75")

    def test_parse_final_balance(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.final_balance == Decimal("2150.75")

    def test_parse_currency(self):
        norma_43_document = FooterParser.parse(self.FOOTER_CONTENT, Norma43Document(), "DMY")
        assert norma_43_document.footer.currency == "978"
